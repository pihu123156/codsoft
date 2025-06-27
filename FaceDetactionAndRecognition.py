import torch
from torchvision import transforms
from facenet_pytorch import MTCNN, InceptionResnetV1
from PIL import Image
import os
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import matplotlib.pyplot as plt

# Device configuration
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

# Load face detector and recognition model
mtcnn = MTCNN(keep_all=False, device=device)
resnet = InceptionResnetV1(pretrained='vggface2').eval().to(device)

# Transformer encoder module (simple example)
import torch.nn as nn

class SimpleTransformer(nn.Module):
    def __init__(self, d_model=512, nhead=8, num_layers=2):
        super(SimpleTransformer, self).__init__()
        encoder_layer = nn.TransformerEncoderLayer(d_model=d_model, nhead=nhead)
        self.encoder = nn.TransformerEncoder(encoder_layer, num_layers=num_layers)
    
    def forward(self, x):
        # x: (batch_size, d_model) → (seq_len, batch, d_model)
        return self.encoder(x.unsqueeze(0)).squeeze(0)

transformer = SimpleTransformer(d_model=512).to(device)

# Preprocess image and extract face embedding
def get_embedding(img_path):
    img = Image.open(img_path).convert('RGB')
    face = mtcnn(img)
    if face is None:
        print("No face detected.")
        return None
    face = face.unsqueeze(0).to(device)  # (1, 3, 160, 160)
    embedding = resnet(face)  # (1, 512)
    refined_embedding = transformer(embedding)  # optional transformer
    return refined_embedding.detach().cpu().numpy()

# Compare embeddings using cosine similarity
def compare_embeddings(emb1, emb2):
    sim = cosine_similarity(emb1, emb2)[0][0]
    return sim

# Example usage
if __name__ == "__main__":
    img1 = "face1.jpg"  # Replace with actual path
    img2 = "face2.jpg"

    emb1 = get_embedding(img1)
    emb2 = get_embedding(img2)

    if emb1 is not None and emb2 is not None:
        similarity = compare_embeddings(emb1, emb2)
        print(f"Cosine Similarity: {similarity:.4f}")
        if similarity > 0.6:
            print("Same person.")
        else:
            print("Different persons.")
