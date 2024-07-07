

from PIL import Image, ImageEnhance
from genZip import zip_folder


def templatedesign1_2_3(backgroundImagePath, logoPath, logo2Path, linepath, ccPath, hodPath):
  print(f"\nIn templatedesign_1_2_3()")

  background_image = Image.open(backgroundImagePath).convert('RGBA')
  a4_width = 3508
  a4_height = 2480
  background_image = background_image.resize((a4_width, a4_height), Image.LANCZOS)
  # print(f"Final Bg image resolution is: {background_image.size}")


  logo_image1 = Image.open(logoPath).convert('RGBA')  # Ensure RGBA mode
  logo_width, logo_height = logo_image1.size
  if logo_height == logo_width:
    logo1_new_width = int(a4_width/8)
    logo1_new_height = int(a4_height/6)

  else:
    logo1_new_width = int(a4_width/4)
    logo1_new_height = int(a4_height/8)

  logo1_position = (90, 120) 
  logo_image1 = logo_image1.resize((logo1_new_width, logo1_new_height), Image.LANCZOS)
  # print(f"Logo image resolution is: {logo_image1.size}")
  mask = logo_image1.getchannel('A')
  background_image.paste(logo_image1, logo1_position, mask)



  if not (logo2Path == None):
    logo_image2 = Image.open(f"{logo2Path}").convert('RGBA')  # Ensure RGBA mode
    logo2_width, logo2_height = logo_image2.size
    if logo2_height == logo2_width:
      logo2_new_width = int(a4_width/8)
      logo2_new_height = int(a4_height/6)

    else:
      logo2_new_width = int(a4_width/3)
      logo2_new_height = int(a4_height/5)

    logo2_position = (2800, 1950) 
    logo_image2 = logo_image2.resize((logo2_new_width, logo2_new_height), Image.LANCZOS)
    mask2 = logo_image2.getchannel('A')
    background_image.paste(logo_image2, logo2_position, mask2)



  cc_sign = Image.open(f"{ccPath}").convert('RGBA')  # Ensure RGBA mode
  cc_sign_width = int(a4_width/9)
  cc_sign_height = int(a4_height/10)
  position3 = (1000, 1900)
  cc_sign = cc_sign.resize((cc_sign_width, cc_sign_height), Image.LANCZOS)
  mask3 = cc_sign.getchannel('A')
  background_image.paste(cc_sign, position3, mask3)



  hod_sign = Image.open(f"{hodPath}").convert('RGBA')  # Ensure RGBA mode
  hod_sign_width = int(a4_width/9)
  hod_sign_height = int(a4_height/10)
  position4 = (2050, 1900)
  hod_sign = hod_sign.resize((hod_sign_width, hod_sign_height), Image.LANCZOS)
  mask4 = hod_sign.getchannel('A')
  background_image.paste(hod_sign, position4, mask4)



  line1 = Image.open(f"{linepath}").convert('RGBA')  # Ensure RGBA mode
  line1_width = int(a4_width/5)
  line1_height = int(a4_height/5)
  position5 = (850, 1900)
  line1 = line1.resize((line1_width, line1_height), Image.LANCZOS)
  mask5 = line1.getchannel('A')
  background_image.paste(line1, position5, mask5)



  line2 = Image.open(f"{linepath}").convert('RGBA')  # Ensure RGBA mode
  line2_width = int(a4_width/5)
  line2_height = int(a4_height/5)
  position6 = (1850, 1900)
  line2 = line2.resize((line2_width, line2_height), Image.LANCZOS)
  mask6 = line2.getchannel('A')
  background_image.paste(line2, position6, mask6)


  # Paste the logo image with transparency mask

  # Save the resulting image as PNG
  output_image_path = f"./static/Images/CertificateEssentials/FinalTemplate/finalTemplate.png"
  background_image.save(output_image_path, quality=75)
  background_image.save(output_image_path, format='PNG')
  return output_image_path


# -----------------------------------------------------------------------------


def templatedesign4(backgroundImagePath, logoPath, logo2Path, linepath, ccPath, hodPath):
  print(f"\nIn templatedesign4()")

  background_image = Image.open(backgroundImagePath).convert('RGBA')
  a4_width = 3508
  a4_height = 2480
  background_image = background_image.resize((a4_width, a4_height), Image.LANCZOS)
  # print(f"Final Bg image resolution is: {background_image.size}")



  logo_image1 = Image.open(logoPath).convert('RGBA')  # Ensure RGBA mode
  logo_width, logo_height = logo_image1.size
  if logo_height == logo_width:
    logo1_new_width = int(a4_width/8)
    logo1_new_height = int(a4_height/6)

  else:
    logo1_new_width = int(a4_width/4)
    logo1_new_height = int(a4_height/8)

  logo1_position = (30, 2200) 
  logo_image1 = logo_image1.resize((logo1_new_width, logo1_new_height), Image.LANCZOS)
  # print(f"Logo image resolution is: {logo_image1.size}")
  mask = logo_image1.getchannel('A')
  background_image.paste(logo_image1, logo1_position, mask)



  if not(logo2Path == None):
    logo_image2 = Image.open(f"{logo2Path}").convert('RGBA')  # Ensure RGBA mode
    logo2_width, logo2_height = logo_image2.size
    if logo2_height == logo2_width:
      logo2_new_width = int(a4_width/8)
      logo2_new_height = int(a4_height/6)

    else:
      logo2_new_width = int(a4_width/3)
      logo2_new_height = int(a4_height/5)

    logo2_position = (3100, 3) 
    logo_image2 = logo_image2.resize((logo2_new_width, logo2_new_height), Image.LANCZOS)
    mask2 = logo_image2.getchannel('A')
    background_image.paste(logo_image2, logo2_position, mask2)



  cc_sign = Image.open(f"{ccPath}").convert('RGBA')  # Ensure RGBA mode
  cc_sign_width = int(a4_width/9)
  cc_sign_height = int(a4_height/10)
  position3 = (1000, 1900)
  cc_sign = cc_sign.resize((cc_sign_width, cc_sign_height), Image.LANCZOS)
  mask3 = cc_sign.getchannel('A')
  background_image.paste(cc_sign, position3, mask3)
  



  hod_sign = Image.open(f"{hodPath}").convert('RGBA')  # Ensure RGBA mode
  hod_sign_width = int(a4_width/9)
  hod_sign_height = int(a4_height/10)
  position4 = (2050, 1900)
  hod_sign = hod_sign.resize((hod_sign_width, hod_sign_height), Image.LANCZOS)
  mask4 = hod_sign.getchannel('A')
  background_image.paste(hod_sign, position4, mask4)



  line1 = Image.open(f"{linepath}").convert('RGBA')  # Ensure RGBA mode
  line1_width = int(a4_width/5)
  line1_height = int(a4_height/5)
  position5 = (950, 1900)
  line1 = line1.resize((line1_width, line1_height), Image.LANCZOS)
  mask5 = line1.getchannel('A')
  background_image.paste(line1, position5, mask5)



  line2 = Image.open(f"{linepath}").convert('RGBA')  # Ensure RGBA mode
  line2_width = int(a4_width/5)
  line2_height = int(a4_height/5)
  position6 = (1860, 1900)
  line2 = line2.resize((line2_width, line2_height), Image.LANCZOS)
  mask6 = line2.getchannel('A')
  background_image.paste(line2, position6, mask6)


  # Save the resulting image as PNG
  output_image_path = f"./static/Images/CertificateEssentials/FinalTemplate/finalTemplate.png"
  background_image.save(output_image_path, quality=75)
  background_image.save(output_image_path, format='PNG')
  return output_image_path


# ------------------------------------------------------------------------------------------------------------

def templatedesign5(backgroundImagePath, logoPath, logo2Path, linepath, ccPath, hodPath):
  print(f"\nIn templatedesign5()")

  background_image = Image.open(backgroundImagePath).convert('RGBA')
  a4_width = 3508
  a4_height = 2480
  background_image = background_image.resize((a4_width, a4_height), Image.LANCZOS)
  print(f"Final Bg image resolution is: {background_image.size}")


  logo_image1 = Image.open(logoPath).convert('RGBA')  # Ensure RGBA mode
  logo_width, logo_height = logo_image1.size
  if logo_height == logo_width:
    logo1_new_width = int(a4_width/12)
    logo1_new_height = int(a4_height/8)

  else:
    logo1_new_width = int(a4_width/4)
    logo1_new_height = int(a4_height/8)

  logo1_position = (1609, 518) 
  logo_image1 = logo_image1.resize((logo1_new_width, logo1_new_height), Image.LANCZOS)
  print(f"Logo image resolution is: {logo_image1.size}")
  mask = logo_image1.getchannel('A')
  background_image.paste(logo_image1, logo1_position, mask)



  if not (logo2Path == None):
    logo_image2 = Image.open(f"{logo2Path}").convert('RGBA')  # Ensure RGBA mode
    logo2_width, logo2_height = logo_image2.size
    print(f"Logo2 image resolution is: {logo_image2.size}")

    if logo2_height == logo2_width:
      logo2_new_width = int(a4_width/10)
      logo2_new_height = int(a4_height/8)

    else:
      logo2_new_width = int(a4_width/3)
      logo2_new_height = int(a4_height/5)

    logo2_position = (550, 2000) 
    logo_image2 = logo_image2.resize((logo2_new_width, logo2_new_height), Image.LANCZOS)
    mask2 = logo_image2.getchannel('A')
    background_image.paste(logo_image2, logo2_position, mask2)



  cc_sign = Image.open(f"{ccPath}").convert('RGBA')  # Ensure RGBA mode
  cc_sign_width = int(a4_width/9)
  cc_sign_height = int(a4_height/12)
  position3 = (1150, 1900)
  cc_sign = cc_sign.resize((cc_sign_width, cc_sign_height), Image.LANCZOS)
  mask3 = cc_sign.getchannel('A')
  background_image.paste(cc_sign, position3, mask3)



  hod_sign = Image.open(f"{hodPath}").convert('RGBA')  # Ensure RGBA mode
  hod_sign_width = int(a4_width/9)
  hod_sign_height = int(a4_height/12)
  position4 = (2050, 1900)
  hod_sign = hod_sign.resize((hod_sign_width, hod_sign_height), Image.LANCZOS)
  mask4 = hod_sign.getchannel('A')
  background_image.paste(hod_sign, position4, mask4)



  line1 = Image.open(f"{linepath}").convert('RGBA')  # Ensure RGBA mode
  line1_width = int(a4_width/5)
  line1_height = int(a4_height/5)
  position5 = (1050, 1900)
  line1 = line1.resize((line1_width, line1_height), Image.LANCZOS)
  mask5 = line1.getchannel('A')
  background_image.paste(line1, position5, mask5)



  line2 = Image.open(f"{linepath}").convert('RGBA')  # Ensure RGBA mode
  line2_width = int(a4_width/5)
  line2_height = int(a4_height/5)
  position6 = (1900, 1900)
  line2 = line2.resize((line2_width, line2_height), Image.LANCZOS)
  mask6 = line2.getchannel('A')
  background_image.paste(line2, position6, mask6)


  # Paste the logo image with transparency mask

  # Save the resulting image as PNG
  output_image_path = f"./static/Images/CertificateEssentials/FinalTemplate/finalTemplate.png"
  background_image.save(output_image_path, quality=75)
  background_image.save(output_image_path, format='PNG')
  return output_image_path

# ------------------------------------------------------------------------------------------------------------


def templatedesign2b(backgroundImagePath, logoPath, ccPath, hodPath):

    # Open the images:
    background_image = Image.open(backgroundImagePath).convert('RGBA')


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

    # print(f"Image created successfully! Saved as: {output_image_path}")

    return output_image_path

# -----------------------------------------------------------------------------