

from PIL import Image, ImageEnhance
from genZip import zip_folder

def templatedesign(backgroundImagePath, logoPath, logo2Path, linepath, ccPath, hodPath):
  print(f"in starting of templatedesign()")

  background_image = Image.open(backgroundImagePath)
  a4_width = 3508
  a4_height = 2480
  background_image = background_image.resize((a4_width, a4_height), Image.LANCZOS)
  print(f"Final Bg image resolution is: {background_image.size}")


  logo_image1 = Image.open(logoPath).convert('RGBA')  # Ensure RGBA mode
  logo_width, logo_height = logo_image1.size
  if logo_height == logo_width:
    logo1_new_width = int(a4_width/8)
    logo1_new_height = int(a4_height/6)

  else:
    logo1_new_width = int(a4_width/4)
    logo1_new_height = int(a4_height/6)

  logo1_position = (90, 90) 
  logo_image1 = logo_image1.resize((logo1_new_width, logo1_new_height), Image.LANCZOS)
  print(f"Logo image resolution is: {logo_image1.size}")


  logo_image2 = Image.open(f"{logo2Path}").convert('RGBA')  # Ensure RGBA mode
  logo_width, logo_height = logo_image2.size
  if logo_height == logo_width:
    logo2_new_width = int(a4_width/8)
    logo2_new_height = int(a4_height/6)

  else:
    logo2_new_width = int(a4_width/3)
    logo2_new_height = int(a4_height/5)

  logo2_position = (2800, 1950) 
  logo_image2 = logo_image2.resize((logo2_new_width, logo2_new_height), Image.LANCZOS)
  print(f"Logo2 image resolution is: {logo_image1.size}")


  cc_sign = Image.open(f"{ccPath}").convert('RGBA')  # Ensure RGBA mode
  cc_sign_width = int(a4_width/9)
  cc_sign_height = int(a4_height/10)
  position3 = (1000, 1900)
  cc_sign = cc_sign.resize((cc_sign_width, cc_sign_height), Image.LANCZOS)


  hod_sign = Image.open(f"{hodPath}").convert('RGBA')  # Ensure RGBA mode
  hod_sign_width = int(a4_width/9)
  hod_sign_height = int(a4_height/10)
  position4 = (2050, 1900)
  hod_sign = hod_sign.resize((hod_sign_width, hod_sign_height), Image.LANCZOS)


  line1 = Image.open(f"{linepath}").convert('RGBA')  # Ensure RGBA mode
  line1_width = int(a4_width/5)
  line1_height = int(a4_height/5)
  position5 = (850, 1900)
  line1 = line1.resize((line1_width, line1_height), Image.LANCZOS)


  line2 = Image.open(f"{linepath}").convert('RGBA')  # Ensure RGBA mode
  line2_width = int(a4_width/5)
  line2_height = int(a4_height/5)
  position6 = (1850, 1900)
  line2 = line2.resize((line2_width, line2_height), Image.LANCZOS)


  # Get a mask from the alpha channel
  mask = logo_image1.getchannel('A')
  mask2 = logo_image2.getchannel('A')
  mask3 = cc_sign.getchannel('A')
  mask4 = hod_sign.getchannel('A')
  mask5 = line1.getchannel('A')
  mask6 = line2.getchannel('A')

  # Paste the logo image with transparency mask
  background_image.paste(logo_image1, logo1_position, mask)
  background_image.paste(logo_image2, logo2_position, mask2)
  background_image.paste(cc_sign, position3, mask3)
  background_image.paste(hod_sign, position4, mask4)
  background_image.paste(line1, position5, mask5)
  background_image.paste(line2, position6, mask6)

  # Save the resulting image as PNG
  output_image_path = f"./static/Images/CertificateEssentials/FinalTemplate/finalTemplate.png"
  background_image.save(output_image_path, quality=75)
  background_image.save(output_image_path, format='PNG')

  # comp_zip_path = f"./static/Images/CertificateEssentials/finalTemplate.zip"
  # zip_folder(f"./static/Images/CertificateEssentials/FinalTemplate", comp_zip_path)
  # print(f"Compress Template created...")
  # print(f"Image created successfully! Saved as: {output_image_path}")
  # print(f"in end of templatedesign()...")
  # compressed_final_template = f"./static/Images/CertificateEssentials/finalTemplate.zip/finalTemplate.png"
  # return compressed_final_template
  
  from compress_image import compress_image
  output_image_path = compress_image(output_image_path, f"./static/Images/CertificateEssentials/FinalTemplate/CompressedFinalTemplate.png", 1000)
  return output_image_path

# -----------------------------------------------------------------------------

def templatedesign2(backgroundImagePath, logoPath, ccPath, hodPath):

    # Open the images:
    background_image = Image.open(backgroundImagePath)


    cc_sign = Image.open(f"{ccPath}").convert('RGBA')  # Ensure RGBA mode
    cc_sign_width = 700
    cc_sign_height = 200
    position3 = (950, 1950)
    cc_sign = cc_sign.resize((cc_sign_width, cc_sign_height), Image.LANCZOS)

    hod_sign = Image.open(f"{hodPath}").convert('RGBA')  # Ensure RGBA mode
    hod_sign_width = 800
    hod_sign_height = 200
    position4 = (1900, 1950)
    hod_sign = hod_sign.resize((hod_sign_width, hod_sign_height), Image.LANCZOS)

    # Get a mask from the alpha channel
    mask3 = cc_sign.getchannel('A')
    mask4 = hod_sign.getchannel('A')

    # Paste the images with transparency mask:
    background_image.paste(cc_sign, position3, mask3)
    background_image.paste(hod_sign, position4, mask4)

    # Save the resulting image as PNG
    output_image_path = "./static/Images/finalTemplate.png"
    background_image.save(output_image_path, quality=75)
    background_image.save(output_image_path, format='PNG')

    print(f"Image created successfully! Saved as: {output_image_path}")

    return output_image_path

# -----------------------------------------------------------------------------
# def templatedesign3(backgroundImagePath, logoPath, ccPath, hodPath):
#   # Open the images
#   background_image = Image.open(backgroundImagePath)

#   overlay_image = Image.open(logoPath).convert('RGBA')  # Ensure RGBA mode
#   overlay_image2 = Image.open(f"./static/Images/CertificateEssentials/TechGeeksLogoColor.png").convert('RGBA')  # Ensure RGBA mode

#   cc_sign = Image.open(f"{ccPath}").convert('RGBA')  # Ensure RGBA mode
#   hod_sign = Image.open(f"{hodPath}").convert('RGBA')  # Ensure RGBA mode

#   line1 = Image.open(f"./static/Images/CertificateEssentials/line1b.png").convert('RGBA')  # Ensure RGBA mode
# #   line2 = Image.open(f"./static/Images/CertificateEssentials/line2.png").convert('RGBA')  # Ensure RGBA mode

#   # Get the original width of the logo image
#   logo_width, logo_height = overlay_image.size
#   print(f"\t\tlogo width is: {logo_width}")
#   print(f"\t\tlogo_height is: {logo_height}")
  
#   if 4000 <= logo_width < 4500:
#         new_Logo_width = 500

#   elif 3500 <= logo_width < 4000:
#       new_Logo_width = 250

#   elif 3000 <= logo_width < 3500:
#       new_Logo_width = 200

#   elif 2500 <= logo_width < 3000:
#       new_Logo_width = 150

#   elif 2000 <= logo_width < 2500:
#       new_Logo_width = 100

#   elif 500 <= logo_width < 2000:
#       new_Logo_width = 50

#   elif 0 <= logo_width < 500:
#       new_Logo_width = 30

#   # Resize the logo image
#   # new_width = 2100

#   new_Logo_height = 200
#   position = (30, 70) 
#   overlay_image = overlay_image.resize((new_Logo_width, new_Logo_height), Image.LANCZOS)

#   new_Logo2_width = 270
#   new_Logo2_height = 180
#   position2 = (1725, 1195)
#   overlay_image2 = overlay_image2.resize((new_Logo2_width, new_Logo2_height), Image.LANCZOS)

#   cc_sign_width = 400
#   cc_sign_height = 100
#   position3 = (500, 1130)
#   cc_sign = cc_sign.resize((cc_sign_width, cc_sign_height), Image.LANCZOS)

#   hod_sign_width = 400
#   hod_sign_height = 100
#   position4 = (1100, 1130)
#   hod_sign = hod_sign.resize((hod_sign_width, hod_sign_height), Image.LANCZOS)

#   line1_width = 600
#   line1_height = 900
#   position5 = (400, 775)
#   line1 = line1.resize((line1_width, line1_height), Image.LANCZOS)

# #   line2_width = 1700
# #   line2_height = 900
#   position6 = (970, 775)
# #   line2 = line2.resize((line2_width, line2_height), Image.LANCZOS)


#   # Get a mask from the alpha channel
#   mask = overlay_image.getchannel('A')
#   mask2 = overlay_image2.getchannel('A')
#   mask3 = cc_sign.getchannel('A')
#   mask4 = hod_sign.getchannel('A')
#   mask5 = line1.getchannel('A')
# #   mask6 = line2.getchannel('A')

#   # Paste the logo image with transparency mask
#   background_image.paste(overlay_image, position, mask)
#   background_image.paste(overlay_image2, position2, mask2)
#   background_image.paste(cc_sign, position3, mask3)
#   background_image.paste(hod_sign, position4, mask4)
#   background_image.paste(line1, position5, mask5)
#   background_image.paste(line1, position6, mask5)

#   # Save the resulting image as PNG
#   output_image_path = "./static/Images/finalTemplate.png"
#   background_image.save(output_image_path, quality=75)
#   background_image.save(output_image_path, format='PNG')

#   print(f"Image created successfully! Saved as: {output_image_path}")

#   return output_image_path
