from flask import Flask, render_template, send_file
import numpy as np
import matplotlib.pyplot as plt
import io
import random

app = Flask(__name__)


# Ana sayfa route'u
@app.route('/')
def index():
    return render_template('index.html')


# Grafik oluşturma ve gösterme
@app.route('/generate_plot')
def generate_plot():
    num_points = 1000
    grid_size = 100
    x_koordinat = np.random.randint(0, 1001, size=num_points)
    y_koordinat = np.random.randint(0, 1001, size=num_points)

    plt.figure(figsize=(10, 10))

    # Her bir hücreye rastgele bir renk atayalım
    colors = np.random.rand(1001 // grid_size, 1001 // grid_size, 3)

    for i in range(1001 // grid_size):
        for j in range(1001 // grid_size):
            mask = (x_koordinat >= i * grid_size) & (x_koordinat < (i + 1) * grid_size) & \
                   (y_koordinat >= j * grid_size) & (y_koordinat < (j + 1) * grid_size)
            plt.scatter(x_koordinat[mask], y_koordinat[mask], color=colors[i, j], s=10)

    plt.xticks(np.arange(0, 1001, grid_size))
    plt.yticks(np.arange(0, 1001, grid_size))
    plt.grid(True)

    plt.xlabel('X Koordinatları')
    plt.ylabel('Y Koordinatları')
    plt.title(f'Rastgele Noktaların Dağılımı (Izgara Boyutu: {grid_size}x{grid_size})')

    # Görseli byte stream olarak kaydedelim
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)

    plt.close()
    return send_file(img, mimetype='image/png')


if __name__ == '__main__':
    app.run(debug=True)
