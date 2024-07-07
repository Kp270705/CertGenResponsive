from fpdf import FPDF
import os
import shutil
import datetime as dt
import asyncio

# fonts_truetype = f"/usr/share/fonts/truetype"
fonts_truetype_Poppins = f"/usr/share/fonts/truetype/Poppins"
fonts_truetype_Montserrat = f"/usr/share/fonts/truetype/Montserrat"
fonts_truetype_edu = f"/usr/share/fonts/truetype/Edu_NSW_ACT_Foundation"
fonts_truetype_meriweath = f"/usr/share/fonts/truetype/Merriweath"

# random:
eufm = f"/usr/share/fonts/truetype/lyx"
greatvibes = f"/usr/share/fonts/truetype/Great_Vibes"
Playfair = f"/usr/share/fonts/truetype/Playfair"


FONTS = {
        # poppins:
        "Poppins" :  {
            "poppinsExtraBold":f"{fonts_truetype_Poppins}/Poppins-ExtraBold.ttf",
            "poppinsBold":f"{fonts_truetype_Poppins}/Poppins-Bold.ttf",
            "poppinsMedium":f"{fonts_truetype_Poppins}/Poppins-Medium.ttf",
            "poppinsLight":f"{fonts_truetype_Poppins}/Poppins-Light.ttf",
            "poppinsExtraLight":f"{fonts_truetype_Poppins}/Poppins-ExtraLight.ttf",
            "poppinsRegular":f"{fonts_truetype_Poppins}/Poppins-Regular.ttf",
            "poppinsSemiBold":f"{fonts_truetype_Poppins}/Poppins-SemiBold.ttf"
        },
        # MontSerrat:
        "Montserrat" : {
            "MontserratBlack": f"{fonts_truetype_Montserrat}/Montserrat-Black.ttf",
            "MontserratBold" : f"{fonts_truetype_Montserrat}/Montserrat-Bold.ttf",
            "MontserratExtraBold" : f"{fonts_truetype_Montserrat}/Montserrat-ExtraBold.ttf",
            "MontserratSemiBold" : f"{fonts_truetype_Montserrat}/Montserrat-SemiBold.ttf",
            "MontserratExtraLight" : f"{fonts_truetype_Montserrat}/Montserrat-ExtraLight.ttf",
            "MontserratLight" : f"{fonts_truetype_Montserrat}/Montserrat-Light.ttf",
            "MontserratMedium" : f"{fonts_truetype_Montserrat}/Montserrat-Medium.ttf",
            "MontserratRegular" : f"{fonts_truetype_Montserrat}/Montserrat-Regular.ttf",
            "MontserratThin" : f"{fonts_truetype_Montserrat}/Montserrat-Thin.ttf"
        },

        "edu" :{
            "ENAF" : f"{fonts_truetype_edu}/EduNSWACTFoundation-VariableFont_wght.ttf",

        }, 

        "Merriweath":{
            "MerriBlack": f"{fonts_truetype_meriweath}/Merriweather-Black.ttf",
            "MerriBold": f"{fonts_truetype_meriweath}/Merriweather-Bold.ttf",
            "MerriLight": f"{fonts_truetype_meriweath}/Merriweather-Light.ttf",
            "MerriRegular": f"{fonts_truetype_meriweath}/Merriweather-Regular.ttf",
        }, 

        "RandomFonts":{
            "eufm10" : f"{eufm}/eufm10.ttf",
            "GreatVibeReg": f"{greatvibes}/GreatVibes-Regular.ttf" ,
            "Playfair" : f"{Playfair}/PlayfairDisplay-VariableFont_wght.ttf"
        }

}

def add_spacing(input_string, spacing):
    """
    Add spacing between characters in a string.

    Args:
    input_string (str): The input string.
    spacing (int): The number of spaces to add between characters.

    Returns:
    str: The input string with spacing added between characters.
    """
    spaced_string = ""
    for char in input_string:
        spaced_string += char + " " * spacing
    return spaced_string

class PDF(FPDF):
    
    def header(self):
        # Add logo or header here if needed
        pass
    
    def footer(self):
        # Add footer here if needed
        pass 

    def load_fonts(self):
        #adding fonts:        
        # poppins:
        self.add_font('Poppins-ExtraBold', "B", f"{FONTS['Poppins']['poppinsExtraBold']}" , uni=True)
        self.add_font('Poppins-Bold', "B", f"{FONTS['Poppins']['poppinsBold']}" , uni=True)
        self.add_font('Poppins-Medium', "", f"{FONTS['Poppins']['poppinsMedium']}" , uni=True)
        self.add_font('Poppins-Light', "", f"{FONTS['Poppins']['poppinsExtraLight']}" , uni=True)
        self.add_font('Poppins-ExtraLight', "", f"{FONTS['Poppins']['poppinsLight']}" , uni=True)
        self.add_font('Poppins-Regular', "", f"{FONTS['Poppins']['poppinsRegular']}" , uni=True)
        self.add_font('Poppins-SemiBold', "B", f"{FONTS['Poppins']['poppinsSemiBold']}" , uni=True)

        # montserrat:
        self.add_font("Montserrat-Black", "", f"{FONTS['Montserrat']['MontserratBlack']}", uni=1 )
        self.add_font("Montserrat-Bold", "B", f"{FONTS['Montserrat']['MontserratBold']}", uni=1 )
        self.add_font("Montserrat-SemiBold", "B", f"{FONTS['Montserrat']['MontserratSemiBold']}", uni=1 )
        self.add_font("Montserrat-ExtraBold", "B", f"{FONTS['Montserrat']["MontserratExtraBold"]}", uni=1 )
        self.add_font("Montserrat-Regular", "", f"{FONTS['Montserrat']["MontserratRegular"]}", uni=1 )
        self.add_font("Montserrat-Thin", "", f"{FONTS['Montserrat']["MontserratThin"]}", uni=1 )
        self.add_font("Montserrat-Medium", "", f"{FONTS['Montserrat']["MontserratMedium"]}", uni=1 )


        self.add_font("Merriweather-Black", "", f"{FONTS['Merriweath']['MerriBlack']}", uni=1 )
        self.add_font("Merriweather-Bold", "B", f"{FONTS['Merriweath']['MerriBold']}", uni=1 )
        self.add_font("Merriweather-Light", "B", f"{FONTS['Merriweath']['MerriLight']}", uni=1 )
        self.add_font("Merriweather-Regular", "", f"{FONTS['Merriweath']['MerriRegular']}", uni=1 )

        #random
        self.add_font("eufm10", "", f"{FONTS['RandomFonts']['eufm10']}", uni=1 )
        self.add_font("GreatVibes-Regular", "", f"{FONTS['RandomFonts']['GreatVibeReg']}", uni=1 )
        self.add_font("PlayfairDisplay-VariableFont_wght", "", f"{FONTS['RandomFonts']['Playfair']}", uni=1 )    
        
# certificate design1:-        
    def certificate1(self, name, sId, receiver_mail, course, sem, date, eventname, orgname, i, certType, certificateChoice, opertype, text_color, organizer1_designation, organizer2_designation, PDF_bg):
        print(f"in certificate1 method...(of gen_pdf)")
        # date= dt.date.today()
        date=date
        
        # Add page with landscape orientation
        self.add_page(orientation="L")
        
        w = self.w
        h = self.h

        # Calculate margins and text width for centering (optional)
        left_margin = 20  # Adjust this value for desired left padding
        right_margin = self.w - left_margin  # Calculate right margin based on page width
        
        print(f"applying image to pdf")
        self.image(f"{PDF_bg}", 0, 0, w, h)
        print(f"image added successfully.")

        print(f"...started adding font")
        self.load_fonts()
        # #adding fonts:        
        # # poppins:
        # self.add_font('Poppins-ExtraBold', "B", f"{FONTS['Poppins']['poppinsExtraBold']}" , uni=True)
        # self.add_font('Poppins-Bold', "B", f"{FONTS['Poppins']['poppinsBold']}" , uni=True)
        # self.add_font('Poppins-Medium', "", f"{FONTS['Poppins']['poppinsMedium']}" , uni=True)
        # self.add_font('Poppins-Light', "", f"{FONTS['Poppins']['poppinsExtraLight']}" , uni=True)
        # self.add_font('Poppins-ExtraLight', "", f"{FONTS['Poppins']['poppinsLight']}" , uni=True)
        # self.add_font('Poppins-Regular', "", f"{FONTS['Poppins']['poppinsRegular']}" , uni=True)
        # self.add_font('Poppins-SemiBold', "B", f"{FONTS['Poppins']['poppinsSemiBold']}" , uni=True)

        # # montserrat:
        # self.add_font("Montserrat-Black", "", f"{FONTS['Montserrat']['MontserratBlack']}", uni=1 )
        # self.add_font("Montserrat-Bold", "B", f"{FONTS['Montserrat']['MontserratBold']}", uni=1 )
        # self.add_font("Montserrat-SemiBold", "B", f"{FONTS['Montserrat']['MontserratSemiBold']}", uni=1 )
        # self.add_font("Montserrat-ExtraBold", "B", f"{FONTS['Montserrat']["MontserratExtraBold"]}", uni=1 )
        # self.add_font("Montserrat-Regular", "", f"{FONTS['Montserrat']["MontserratRegular"]}", uni=1 )
        # self.add_font("Montserrat-Thin", "", f"{FONTS['Montserrat']["MontserratThin"]}", uni=1 )
        # self.add_font("Montserrat-Medium", "", f"{FONTS['Montserrat']["MontserratMedium"]}", uni=1 )
        print(f"all fonts added successfully...")


        # Set font
        self.ln(30)
        # self.section1 = f"C E R T I F I C A T E\n"
        sec1 = f"CERTIFICATE"
        # spacedSection1 = add_spacing(sec1, 1)
        self.section1 = f"{sec1}"
        self.set_font("Montserrat-Bold", size=38, style="B")
        self.set_text_color(text_color)
        self.multi_cell(270, 8, txt=self.section1, align='C')
        self.ln(4)
        
        sec2 = f"{certType.upper()}"
        spacedSection2 = add_spacing(sec2, 1)
        self.section2 = f"{spacedSection2}"
        self.set_font(f"Montserrat-Medium", size=28)
        self.multi_cell(277, 8, txt=self.section2, align='C')
        self.ln(3)
        
        sec3 = f"IS  PROUDLY  PRESENTED  TO"
        # spacedSection3 = add_spacing(sec3, 2)
        self.section3 = f"{sec3}"
        self.set_font("Montserrat-Regular", size=15)
        self.multi_cell(277, 20, txt=self.section3, align='C')
        self.ln(5)
        
        spacedSection4 = add_spacing(name.upper(), 1)
        self.section4 = f"{spacedSection4}"
        self.set_font("Montserrat-Bold", size=30, style="UB")
        self.multi_cell(277, 5, txt=self.section4, align='C')
        self.ln(6)

        spacedSection5a = add_spacing(course.upper(), 2)
        spacedSection5b = add_spacing(sem.upper(), 2)
        self.section5 = f"{spacedSection5a}                     {spacedSection5b}"
        self.set_font("Montserrat-Black", size=18, style="")
        self.multi_cell(277, 10, txt=self.section5, align='C')
        self.ln(10)
        
        # self.section6 = f"F O R   P A R T I C I P A T I N G  I N"
        sec6 = f"FOR  PARTICIPATING  IN"
        # spacedSection6 = add_spacing(sec6, 2)
        self.section6 = f"{sec6}"
        # self.set_font("Poppins-Bold", size=16, style="B")
        self.set_font("Montserrat-Regular", size=18)
        self.multi_cell(277, 8, txt=self.section6, align='C')
        self.ln(10)

        spacedSection7 = add_spacing(eventname.upper(), 1)
        self.section7 = f"{spacedSection7}"
        self.set_font("Poppins-ExtraBold", size=18, style="B")
        self.multi_cell(277, 7, txt=self.section7, align='C')
        self.ln(2)

        sec8 = f"ON"
        spacedSection8 = add_spacing(sec8, 1)
        self.section8 = f"{spacedSection8}"
        self.set_font("Poppins-Regular", size=13)
        self.multi_cell(277, 7, txt=self.section8, align='C')

        self.section9 = f"{date}"
        self.set_font("Poppins-ExtraBold", size=18, style="B")
        self.multi_cell(277, 10, txt=self.section9, align='C')
        self.ln(21)  # Add some space after title

        auth1 = f"        {organizer1_designation}"
        auth2 = f"    {organizer2_designation}"
        spacedSection10a = add_spacing(auth1.upper(), 1)
        spacedSection10b = add_spacing(auth2.upper(), 1)
        self.section10 = f"{spacedSection10a}                   {spacedSection10b}"
        self.set_font("Montserrat-SemiBold", size=10, style="B")
        self.set_left_margin(65)
        self.cell(90, 3, txt=f"{spacedSection10a}", align='C')
        self.set_left_margin(50)
        self.cell(50, 3, txt=f"{spacedSection10b}", align='C')

        print(f"Certificate 1({i}) generated successfully...")


# -----------------------------------------------------------------------------------------------------------------------------------------------------------------

    def certificate2(self, name, sId, receiver_mail, course, sem, date, eventname, orgname, i, certType, certificateChoice, opertype, text_color, organizer1_designation, organizer2_designation, PDF_bg):
        print(f"in certificate2 method.")
        # date= dt.date.today()
        date = date
        
        # Add pag:
        self.add_page(orientation="L")
        w = self.w
        h = self.h
        left_margin = 20  
        right_margin = self.w - left_margin  
        print("Now we adding the image...")
        self.image(f"{PDF_bg}", 0, 0, w, h)
        print("image added successfully...")

        # #adding fonts:        
        # # poppins:
        # self.add_font('Poppins-ExtraBold', "B", f"{FONTS['Poppins']['poppinsExtraBold']}" , uni=True)
        # self.add_font('Poppins-Bold', "B", f"{FONTS['Poppins']['poppinsBold']}" , uni=True)
        # self.add_font('Poppins-Medium', "", f"{FONTS['Poppins']['poppinsMedium']}" , uni=True)
        # self.add_font('Poppins-Light', "", f"{FONTS['Poppins']['poppinsExtraLight']}" , uni=True)
        # self.add_font('Poppins-ExtraLight', "", f"{FONTS['Poppins']['poppinsLight']}" , uni=True)
        # self.add_font('Poppins-Regular', "", f"{FONTS['Poppins']['poppinsRegular']}" , uni=True)
        # self.add_font('Poppins-SemiBold', "B", f"{FONTS['Poppins']['poppinsSemiBold']}" , uni=True)

        # # montserrat:
        # self.add_font("Montserrat-Black", "", f"{FONTS['Montserrat']['MontserratBlack']}", uni=1 )
        # self.add_font("Montserrat-Bold", "B", f"{FONTS['Montserrat']['MontserratBold']}", uni=1 )
        # self.add_font("Montserrat-SemiBold", "B", f"{FONTS['Montserrat']['MontserratSemiBold']}", uni=1 )
        # self.add_font("Montserrat-ExtraBold", "B", f"{FONTS['Montserrat']["MontserratExtraBold"]}", uni=1 )
        # self.add_font("Montserrat-Regular", "", f"{FONTS['Montserrat']["MontserratRegular"]}", uni=1 )
        # self.add_font("Montserrat-Thin", "", f"{FONTS['Montserrat']["MontserratThin"]}", uni=1 )
        # self.add_font("Montserrat-Medium", "", f"{FONTS['Montserrat']["MontserratMedium"]}", uni=1 )

        self.load_fonts()

        # Set font
        self.ln(40)
        # self.section1 = f"C E R T I F I C A T E\n"
        sec1 = f"CERTIFICATE"
        # spacedSection1 = add_spacing(sec1, 1)
        self.section1 = f"{sec1}"
        self.set_font("Montserrat-Bold", size=38, style="B")
        self.set_text_color(text_color)
        self.multi_cell(270, 8, txt=self.section1, align='C')
        self.ln(4)
        
        sec2 = f"{certType.upper()}"
        spacedSection2 = add_spacing(sec2, 1)
        self.section2 = f"{spacedSection2}"
        self.set_font(f"Montserrat-Medium", size=28)
        self.multi_cell(277, 8, txt=self.section2, align='C')
        self.ln(5)
        
        sec3 = f"IS  PROUDLY  PRESENTED  TO"
        # spacedSection3 = add_spacing(sec3, 2)
        self.section3 = f"{sec3}"
        self.set_font("Montserrat-Regular", size=15)
        self.multi_cell(277, 20, txt=self.section3, align='C')
        self.ln(7)
        
        spacedSection4 = add_spacing(name.upper(), 1)
        self.section4 = f"{spacedSection4}"
        self.set_font("Montserrat-Bold", size=25, style="B")
        self.multi_cell(277, 5, txt=self.section4, align='C')
        self.ln(6)

        spacedSection5a = add_spacing(course.upper(), 2)
        spacedSection5b = add_spacing(sem.upper(), 2)
        self.section5 = f"{spacedSection5a}                     {spacedSection5b}"
        self.set_font("Montserrat-Black", size=15, style="")
        self.multi_cell(277, 10, txt=self.section5, align='C')
        self.ln(10)
        
        # self.section6 = f"F O R   P A R T I C I P A T I N G  I N"
        if certType == "of participation":
            sec6 = f"For  participating  in"
        if certType == "Certificate of completion":
            sec6 = f"For  completing  the"
        if certType == "of appreciation":
            sec6 = f"For  completing  the"
        if certType == "of completion":
            sec6 = f"For  completing  the"
            
        # spacedSection6 = add_spacing(sec6, 2)
        self.section6 = f"{sec6}"
        # self.set_font("Poppins-Bold", size=16, style="B")
        self.set_font("Montserrat-Medium", size=15)
        self.multi_cell(277, 8, txt=self.section6, align='C')
        self.ln(1)

        spacedSection7 = add_spacing(eventname.upper(), 0)
        self.section7 = f"{spacedSection7}"
        self.set_font("Poppins-SemiBold", size=18, style="B")
        self.multi_cell(277, 5, txt=self.section7, align='C')
        self.ln(1)

        sec8 = f"ON"
        spacedSection8 = add_spacing(sec8, 1)
        self.section8 = f"{spacedSection8}"
        self.set_font("Poppins-Regular", size=13)
        self.multi_cell(277, 5, txt=self.section8, align='C')
        self.ln(1)

        self.section9 = f"{date}"
        self.set_font("Poppins-SemiBold", size=18, style="B")
        self.multi_cell(277, 6, txt=self.section9, align='C')
        self.ln(24)

        auth1 = f"    {organizer1_designation}"
        auth2 = f"    {organizer2_designation}"
        spacedSection10a = add_spacing(auth1.upper(), 0)
        spacedSection10b = add_spacing(auth2.upper(), 0)
        self.section10 = f"{spacedSection10a}                   {spacedSection10b}"
        self.set_font("Montserrat-Black", size=10, style="")
        self.set_left_margin(60)
        self.cell(100, 3, txt=f"{spacedSection10a}", align='C')
        self.set_left_margin(160)
        self.cell(50, 3, txt=f"{spacedSection10b}", align='C')

        print(f"Certificate2({i}) generated successfully...")       


# --------------------------------------------------------------------------

    def certificate5(self, name, sId, receiver_mail, course, sem, date, eventname, orgname, i, certType, certificateChoice, opertype, text_color, organizer1_designation, organizer2_designation, PDF_bg):
        print(f"in certificate5 method...(of gen_pdf)")
        # date= dt.date.today()
        date = date
        
        # Add page:
        self.add_page(orientation="L")
        w = self.w
        h = self.h
        left_margin = 20  
        right_margin = self.w - left_margin  
        
        print("Now we adding the image...")
        # self.image(f"{PDF_bg}", 0, 0, w, h)
        self.image(f"{PDF_bg}", 0, 0, w, h)
        print("Image added successfully...")

        self.load_fonts()

        # #adding fonts:        
        # # poppins:
        # self.add_font('Poppins-ExtraBold', "B", f"{FONTS['Poppins']['poppinsExtraBold']}" , uni=True)
        # self.add_font('Poppins-Bold', "B", f"{FONTS['Poppins']['poppinsBold']}" , uni=True)
        # self.add_font('Poppins-Medium', "", f"{FONTS['Poppins']['poppinsMedium']}" , uni=True)
        # self.add_font('Poppins-Light', "", f"{FONTS['Poppins']['poppinsExtraLight']}" , uni=True)
        # self.add_font('Poppins-ExtraLight', "", f"{FONTS['Poppins']['poppinsLight']}" , uni=True)
        # self.add_font('Poppins-Regular', "", f"{FONTS['Poppins']['poppinsRegular']}" , uni=True)
        # self.add_font('Poppins-SemiBold', "B", f"{FONTS['Poppins']['poppinsSemiBold']}" , uni=True)

        # # montserrat:
        # self.add_font("Montserrat-Black", "", f"{FONTS['Montserrat']['MontserratBlack']}", uni=1 )
        # self.add_font("Montserrat-Bold", "B", f"{FONTS['Montserrat']['MontserratBold']}", uni=1 )
        # self.add_font("Montserrat-SemiBold", "B", f"{FONTS['Montserrat']['MontserratSemiBold']}", uni=1 )
        # self.add_font("Montserrat-ExtraBold", "B", f"{FONTS['Montserrat']["MontserratExtraBold"]}", uni=1 )
        # self.add_font("Montserrat-Regular", "", f"{FONTS['Montserrat']["MontserratRegular"]}", uni=1 )
        # self.add_font("Montserrat-Thin", "", f"{FONTS['Montserrat']["MontserratThin"]}", uni=1 )
        # self.add_font("Montserrat-Medium", "", f"{FONTS['Montserrat']["MontserratMedium"]}", uni=1 )


        # self.add_font("Merriweather-Black", "", f"{FONTS['Merriweath']['MerriBlack']}", uni=1 )
        # self.add_font("Merriweather-Bold", "B", f"{FONTS['Merriweath']['MerriBold']}", uni=1 )
        # self.add_font("Merriweather-Light", "B", f"{FONTS['Merriweath']['MerriLight']}", uni=1 )
        # self.add_font("Merriweather-Regular", "", f"{FONTS['Merriweath']['MerriRegular']}", uni=1 )

        # #random
        # self.add_font("eufm10", "", f"{FONTS['RandomFonts']['eufm10']}", uni=1 )
        # self.add_font("GreatVibes-Regular", "", f"{FONTS['RandomFonts']['GreatVibeReg']}", uni=1 )
        # self.add_font("PlayfairDisplay-VariableFont_wght", "", f"{FONTS['RandomFonts']['Playfair']}", uni=1 )


        # Set font
        self.ln(20)
        sec1 = f"  CERTIFICATE"
        spacedSection1 = add_spacing(sec1, 3)
        self.section1 = f"{sec1}"
        self.set_font("Merriweather-Bold", size=25, style="B")
        self.set_text_color(2, 63, 48)
        self.multi_cell(270, 8, txt=spacedSection1, align='C')
        self.ln(40)
        
        sec2 = f"{certType.upper()}"
        spacedSection2 = add_spacing(sec2, 1)
        self.section2 = f"{spacedSection2}"
        self.set_font("Merriweather-Regular", size=15)
        self.set_text_color(0)
        self.multi_cell(277, 8, txt=spacedSection2, align='C')
        self.ln(3)
        
        sec3 = f"IS  PROUDLY  PRESENTED  TO"
        self.section3 = f"{sec3}"
        self.set_font("Montserrat-Regular", size=15)
        self.multi_cell(277, 20, txt=self.section3, align='C')
        self.ln(6)
        
        spacedSection4 = add_spacing(name.upper(), 1)
        self.section4 = f"{spacedSection4}"
        self.set_font("Merriweather-Regular", size=25, style="U")
        self.set_text_color(218, 165,32)
        self.multi_cell(277, 5, txt=self.section4, align='C')
        self.ln(6)

        spacedSection5a = add_spacing(course.upper(), 2)
        spacedSection5b = add_spacing(sem.upper(), 2)
        self.section5 = f"{spacedSection5a}                   {spacedSection5b}"
        self.set_font("Montserrat-Black", size=15, style="")
        self.set_text_color(0)
        self.multi_cell(277, 10, txt=self.section5, align='C')
        self.ln(5)
        

        if certType == "of participation":
            sec6 = f"For  participating  in"
        if certType == "Certificate of completion":
            sec6 = f"For  completing  the"
        if certType == "of appreciation":
            sec6 = f"For  completing  the"
        if certType == "of completion":
            sec6 = f"For  completing  the"

        self.section6 = f"{sec6}"
        self.set_font("PlayfairDisplay-VariableFont_wght", size=15)
        self.set_left_margin(105)
        self.cell(18, 8, txt=self.section6, align='L')


        spacedSection7 = add_spacing(eventname, 0)
        self.section7 = f"{spacedSection7}"
        self.set_font("Merriweather-Black", size=15, style="")
        self.set_left_margin(2)
        self.cell(100, 8, txt=self.section7, align='C')
        self.ln(10)


        sec8 = f" ON"
        spacedSection8 = add_spacing(sec8, 1)
        self.section8 = f"{spacedSection8}"
        self.set_font("Poppins-Regular", size=13)
        self.multi_cell(277, 5, txt=self.section8, align='C')
        self.ln(1)

        self.section9 = f" {date}"
        self.set_font("Poppins-SemiBold", size=18, style="B")
        self.multi_cell(277, 6, txt=self.section9, align='C')
        self.ln(20)

        auth1 = f"    {organizer1_designation}"
        auth2 = f"    {organizer2_designation}"
        spacedSection10a = add_spacing(auth1.upper(), 1)
        spacedSection10b = add_spacing(auth2.upper(), 1)
        self.section10 = f"{spacedSection10a}   {spacedSection10b}"
        self.set_font("Montserrat-Black", size=10, style="")
        self.set_left_margin(80)
        self.cell(80, 3, txt=f"{spacedSection10a}", align='C')
        self.set_left_margin(60)
        self.cell(60, 3, txt=f"{spacedSection10b}", align='C')

        print(f"Certificate 5({i}) generated successfully...")

# --------------------------------------------------------------------------     
     
    #  design3   
    def certificateRandom(self, name, sId, receiver_mail, course, sem, date, eventname, orgname, i, certificateChoice, opertype, text_color, PDF_bg):
        print(f"in {certificateChoice}")
        # date= dt.date.today()
        date = date

        # Add page with landscape orientation
        self.add_page(orientation="L")
        
        w = self.w
        h = self.h

        self.image(f"{PDF_bg}", 0, 0, w, h)

        # Calculate margins and text width for centering (optional)
        left_margin = 20 
        right_margin = self.w - left_margin  

        # adding fonts:

        # poppins:
        self.add_font('Poppins-ExtraBold', "B", f"{FONTS['Poppins']['poppinsExtraBold']}" , uni=True)
        self.add_font('Poppins-Bold', "B", f"{FONTS['Poppins']['poppinsBold']}" , uni=True)
        self.add_font('Poppins-Medium', "", f"{FONTS['Poppins']['poppinsMedium']}" , uni=True)
        self.add_font('Poppins-Light', "", f"{FONTS['Poppins']['poppinsExtraLight']}" , uni=True)
        self.add_font('Poppins-ExtraLight', "", f"{FONTS['Poppins']['poppinsLight']}" , uni=True)
        self.add_font('Poppins-Regular', "", f"{FONTS['Poppins']['poppinsRegular']}" , uni=True)
        self.add_font('Poppins-SemiBold', "B", f"{FONTS['Poppins']['poppinsSemiBold']}" , uni=True)

        # montserrat:
        self.add_font("Montserrat-Black", "", f"{FONTS['Montserrat']['MontserratBlack']}", uni=1 )
        self.add_font("Montserrat-Bold", "B", f"{FONTS['Montserrat']['MontserratBold']}", uni=1 )
        self.add_font("Montserrat-SemiBold", "B", f"{FONTS['Montserrat']['MontserratSemiBold']}", uni=1 )
        self.add_font("Montserrat-ExtraBold", "B", f"{FONTS['Montserrat']["MontserratExtraBold"]}", uni=1 )
        self.add_font("Montserrat-Regular", "", f"{FONTS['Montserrat']["MontserratRegular"]}", uni=1 )
        self.add_font("Montserrat-Thin", "", f"{FONTS['Montserrat']["MontserratThin"]}", uni=1 )
        self.add_font("Montserrat-Medium", "", f"{FONTS['Montserrat']["MontserratMedium"]}", uni=1 )

        
        self.ln(96)

        spacedSection4 = add_spacing(name.upper(),0)
        self.section4 = f"{spacedSection4}"
        self.set_font("Montserrat-Bold", size=30, style="B")
        self.set_text_color(0,0,0)
        self.multi_cell(277, 5, txt=self.section4, align='C')
        self.ln(4)

        spacedSection5a = add_spacing(course.upper(), 2)
        spacedSection5b = add_spacing(sem.upper(), 2)
        print(f"course in cer: {spacedSection5a}")
        self.section5 = f"{spacedSection5a}            {spacedSection5b}"
        self.set_font("Montserrat-Black", size=18, style="")
        self.multi_cell(277, 10, txt=self.section5, align='C')
        self.ln(1)
        
        self.section6 = f"FOR  PARTICIPATING  IN"
        self.set_font("Montserrat-Regular", size=15)
        self.multi_cell(277, 12, txt=self.section6, align='C')
        self.ln(1)

        spacedSection7 = add_spacing(eventname.upper(), 1)
        self.section7 = f"{spacedSection7}"
        self.set_font("Poppins-ExtraBold", size=16, style="B")
        self.multi_cell(277, 7, txt=self.section7, align='C')
        self.ln(2)

        self.section8 = f"O N"
        self.set_font("Arial", size=15)
        self.multi_cell(277, 7, txt=self.section8, align='C')
        self.ln(1)

        self.section9 = f"{date}"
        self.set_font("Arial", size=16, style="B")
        self.multi_cell(277, 10, txt=self.section9, align='C')
        self.ln(16)  # Add some space after title
        
        self.section10 = f"HEAD OF DEPARTMENT"
        self.section10 = f"H. O. D."
        self.set_left_margin(60)
        self.set_font("Arial", size=14, style="B")
        self.cell(100, 10, txt=self.section10, align="C")
        
        self.section10 = f"C. C."
        self.set_left_margin(180)
        self.set_font("Arial", size=14, style="B")
        self.cell(180, 10, txt=self.section10, align="L")
    

# --------------------------------------------------------------------------     

async def getData(name, sId, receiverMail, course, sem, date, i, eventname, orgName, certType, certificateChoice, operType, organizer1_designation, organizer2_designation, PDF_TemplatePath):
    print(f"\n\ni={i}")
    
    # Create PDFFolder if it doesn't exist
    if i == 1:
        if os.path.exists("./static/PDFFolder"):
            shutil.rmtree("./static/PDFFolder")
        os.mkdir("./static/PDFFolder")
                
    pdf = PDF()
    pdf.set_left_margin(10)
    pdf.set_right_margin(10)
    pdf.set_top_margin(10)
    pdf.set_auto_page_break(auto=True, margin=15)

    if certificateChoice == "Choice1" or certificateChoice == "Choice2" or certificateChoice == "Choice3" :
        if certificateChoice == "Choice1":
            fontcolor = 220
        if certificateChoice == "Choice2" or certificateChoice == "Choice3":
            fontcolor = 0
        pdf.certificate1(name, sId, receiverMail, course, sem, date, eventname, orgName, i, certType, certificateChoice, operType, fontcolor, organizer1_designation, organizer2_designation, PDF_TemplatePath)
        print(f"success")

    if certificateChoice == "Choice4":
        fontcolor = 220
        pdf.certificate2(name, sId, receiverMail, course, sem, date, eventname, orgName, i, certType, certificateChoice, operType, fontcolor, organizer1_designation, organizer2_designation, PDF_TemplatePath)
        print(f"course: {course}")

    if certificateChoice == "Choice5":
        fontcolor = 220
        pdf.certificate5(name, sId, receiverMail, course, sem, date, eventname, orgName, i, certType, certificateChoice, operType, fontcolor, organizer1_designation, organizer2_designation, PDF_TemplatePath)
        print(f"course: {course}")

    pdf.output(f"./static/PDFFolder/{operType}Certificate{i}.pdf")

    if operType == "Generate":
        from sendingMails import send_mails
        print(f"\nIn sending  mails")
        await send_mails(f"kunalpathak4774@gmail.com", receiverMail, f"./static/PDFFolder/{operType}Certificate{i}.pdf", eventname, certType)
    