import cv2
import numpy as np

# Load the image
image = cv2.imread(r"C:\Users\Geeenior\Desktop\Python Exercises\Project\OpenCV\input.jpg")

if image is None:
    print("Error: Image not found.")
    exit()

# Resize the image
image = cv2.resize(image, (800, 600))

# Create watermark overlay
overlay = image.copy()

# Watermark text
text = "GeeniorDaGreat"

# Font settings
font = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 3
thickness = 1
color = (255, 255, 255)  # White

# Get text size
(text_width, text_height), baseline = cv2.getTextSize(
    text, font, font_scale, thickness
)

# Position watermark (bottom-right corner)
text_x = image.shape[1] - text_width - 20
text_y = image.shape[0] - 20

# Draw watermark on overlay
cv2.putText(
    overlay,
    text,
    (text_x, text_y),
    font,
    font_scale,
    color,
    thickness,
    cv2.LINE_AA
)

# Transparency factor
alpha = 0.5

# Blend overlay with original image
watermarked = cv2.addWeighted(overlay, alpha, image, 1 - alpha, 0)

# Save result
cv2.imwrite("watermarked_image.jpg", watermarked)

# Display result
cv2.imshow("Watermarked Image", watermarked)
cv2.waitKey(0)
cv2.destroyAllWindows()
