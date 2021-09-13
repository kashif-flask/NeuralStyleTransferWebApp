# NeuralStyleTransferWebApp
NeuralStyleTransferWebApp is basically a web app which does what it says :), anyways it's take two images from user , one is content image and other is style image and it basically generate a new image whose content is like of content image but with the style of style image, thus it lets you transform images into different styles.

## How to run the app
1.Either fork or downlod app files.
2.Install all dependencies given in requirements.txt file in cmd using  pip install -r requirements.txt
3.run the file app.py in cmd , you will get local host http://127.0.0.1:5000/ 
4.Now open the url in web browser.

## How to use app
1.Select content image that need to transformed and style image whose style will be used to transform content image.
2.Make sure you only use png,jpeg and jpg format files otherwise it will not accept.
3.Select learning rate at which to update pixels of content image ,default 0.01, smaller the number more steps you require to bring desirable change in your content image but more refined result will be.
4.Select content loss weight and style loss weight, it basically tells how much importance is given to content image's content and style image's style in final generated image.
5.Output image width and height, what shape output image should be, max is 400 size because my GPU of 4GB wasn't allowing bigger image to train ;(.
6.Number of steps of training,it lets you choose number of iterations to update your content image with style image, greater the number of steps better the result will be but it will take longer.
7. Simply click on Submit button.

## Features
- Empty file checked , so you can't give no file and also type of file checked , it only allows png,jpeg and jpg files.
- Once the image generated it will be displayed on screen and you can download it by simply clicking in image.

## Future fetaures
1. Make it more beautiful to look, i wish i was good in web designing :(.
2. Deploy on some web server , it tried to deploy on heroku but free version won't take such a big model (Broke me ;{ ), but people can try deploying on other platform like google cloud platform, you have to provide your card details their.
3. Give user flexibility to choose torchvision model on their own , here i used pretrained VGG19.

## Dependencie
-Flask
-Pytorch
-Torchvision
-Pillow

## What the app looks like
First Page

![alt text](https://github.com/kashif-flask/NeuralStyleTransferWebApp/blob/main/First_page.PNG)

After transform


![alt text](https://github.com/kashif-flask/NeuralStyleTransferWebApp/blob/main/generated.PNG)

