CertificateEssestials = f"./static/Images/CertificateEssentials"
certificate_choice = {
    "Choice1":{
    "TemplatePath" :f"{CertificateEssestials}/cert_theme1.jpg",
    "logo2Path ": f"{CertificateEssestials}/TechGeeksLogo.png",
    "ccPath" : f"{CertificateEssestials}/ccWhite.png",
    "hodPath" : f"{CertificateEssestials}/hodWhite.png",
    "linepath" : f"{CertificateEssestials}/line1.png",
    },

    "Choice2":{
    "TemplatePath" :f"{CertificateEssestials}/cert_theme2.png",
    "logo2Path ": f"{CertificateEssestials}/TechGeeksLogoColor.png",
    "ccPath" : f"{CertificateEssestials}/cc.png",
    "hodPath" : f"{CertificateEssestials}/hod.png",
    "linepath" : f"{CertificateEssestials}/line1b.png",
    },
    "Choice3":{
    "TemplatePath" :f"{CertificateEssestials}/cert_theme3.png",
    "logo2Path ": f"{CertificateEssestials}/TechGeeksLogoColor.png",
    "ccPath" : f"{CertificateEssestials}/cc.png",
    "hodPath" : f"{CertificateEssestials}/hod.png",
    "linepath" : f"{CertificateEssestials}/line1b.png",
    },

    "Choice4":{
    "TemplatePath" :f"{CertificateEssestials}/cert_theme4.png",
    "logo2Path ": f"{CertificateEssestials}/TechGeeksLogo.png",
    "ccPath" : f"{CertificateEssestials}/cc.png",
    "hodPath" : f"{CertificateEssestials}/hod.png",
    "linepath" : f"{CertificateEssestials}/line1g.png",
    },

    "Choice5":{
    "TemplatePath" :f"{CertificateEssestials}/cert_theme5.png",
    "logo2Path ": f"{CertificateEssestials}/TechGeeksLogoColor.png",
    "ccPath" : f"{CertificateEssestials}/cc.png",
    "hodPath" : f"{CertificateEssestials}/hod.png",
    "linepath" : f"{CertificateEssestials}/line1g.png",
    },

}

def get_Choice_data(choice):
    # if choice == certificate_choice[choice]:
    #     print(f"\n\n\n\n\n\nIn get path method...\n\t{certificate_choice[choice]}")
    return certificate_choice[choice]

# print(f"{certificate_choice['Choice1']["TemplatePath"]}")