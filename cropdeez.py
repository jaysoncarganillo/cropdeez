from PIL import Image
import os

def crop_and_scale_images_in_folder():
    folder_path = os.getcwd()
    cropped_folder_path = os.path.join(folder_path, 'cropped')
    os.makedirs(cropped_folder_path, exist_ok=True)
    
    for filename in os.listdir(folder_path):
        if filename.lower().endswith((".jpg", ".jpeg", ".png", ".bmp", ".gif", ".tiff")): 
            img_path = os.path.join(folder_path, filename)
            img = Image.open(img_path)
            
            width, height = img.size
            new_dimension = min(width, height)
            left = (width - new_dimension)/2
            top = (height - new_dimension)/2
            right = (width + new_dimension)/2
            bottom = (height + new_dimension)/2
            img = img.crop((left, top, right, bottom))
            
            img = img.resize((250, 250), Image.LANCZOS)
            
            # Convert image to RGB before saving as JPEG
            if img.mode in ("RGBA", "P"): 
                img = img.convert("RGB")
            
            img.save(os.path.join(cropped_folder_path, filename.rsplit('.', 1)[0] + '.jpg'), 'JPEG', quality=80)
            print(f"Cropped and saved image: {os.path.join(cropped_folder_path, filename.rsplit('.', 1)[0] + '.jpg')}")

crop_and_scale_images_in_folder()
