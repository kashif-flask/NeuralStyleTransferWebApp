from flask import Flask

UPLOAD_FOLDER = 'static/uploads/'

app = Flask(__name__)
app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

import os

from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
from main import *
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def file_ext(filename):
    return filename.rsplit('.',1)[1].lower()

@app.route('/')
def upload_form():
    return render_template('upload.html')


@app.route('/', methods=['POST'])
def upload_image():
    total_steps = int(request.form["steps"])
    learning_rate = float(request.form["lr"])
    alpha = float(request.form["alpha"])
    beta = float(request.form["beta"])
    image_width = int(request.form["img_width"])
    image_height = int(request.form["img_height"])
    loader = transforms.Compose([
        transforms.Resize((image_height, image_width)),
        transforms.ToTensor(),
    ])

    def load_image(image_name):
        image = Image.open(image_name)
        image = loader(image).unsqueeze(0)
        return image.to(device)
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    file = request.files['file']
    file1= request.files['file1']
    if file.filename == '':
        flash('No Content image selected for uploading')
        return redirect(request.url)
    if file1.filename == '':
        flash('No Style image selected for uploading')
        return redirect(request.url)
    if file and file1 and allowed_file(file.filename) and allowed_file(file1.filename):
        filename = secure_filename(file.filename)
        content_img = load_image(file)
        style_img = load_image(file1)
        generated_img = content_img.clone().requires_grad_(True)
        optimizer = optim.Adam([generated_img], lr=learning_rate)
        try:
            for step in range(total_steps):
                generated_img_features = model(generated_img)
                content_img_features = model(content_img)
                style_img_features = model(style_img)
                style_loss = content_loss = 0
                for gen, cont, styl in zip(generated_img_features, content_img_features, style_img_features):
                    batch_size, channel, height, width = gen.shape
                    content_loss += torch.mean((gen - cont) ** 2)

                    # compute gram matrix
                    gen_gram = gen.view(channel, width * height).mm(gen.view(channel, width * height).t())
                    styl_gram = styl.view(channel, width * height).mm(styl.view(channel, width * height).t())
                    style_loss += torch.mean((gen_gram - styl_gram) ** 2)
                total_loss = alpha * content_loss + beta * style_loss
                optimizer.zero_grad()
                total_loss.backward()
                optimizer.step()
        except Exception as e:
            flash("someting went wrong")




        # print('upload_image filename: ' + filename)
        save_image(generated_img, os.path.join(app.config['UPLOAD_FOLDER'], filename))
        flash('Image successfully transformed , CLick on the image to download')
        return render_template('upload.html', filename=filename)
    else:
        flash('Allowed image types are -> png, jpg, jpeg')
        return redirect(request.url)


@app.route('/display/<filename>')
def display_image(filename):
    # print('display_image filename: ' + filename)
    return redirect(url_for('static', filename='uploads/' + filename), code=301)


if __name__ == "__main__":
    app.run(debug=True)