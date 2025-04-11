def dox(reason, name, username, alias, current_address, previous_address1, ip, isp, area_code, phone_number, emails, passwords, language, dob, age, race, gender, sexual_orientation, religion, ssn, discord, instagram, twitter, snapchat, mother_name, mother_age, mother_dob, mother_number, mother_address, mother_emails, mother_passwords, mother_ssn, mother_facebook, mother_linkedin, mother_instagram, mother_twitter, father_name, father_dob, father_age, father_number, father_address, father_emails, father_passwords, father_ssn, father_facebook, father_linkedin, father_instagram, father_twitter):
    global doxquestions
    aliases = ", ".join(alias)
    doxquestions = f'''

{reason}

                      BASIC INFO
╔───────────────────────────────────────────────────────╗
     ➤ Name: {name}      
     ➤ Age: {age}
     ➤ DOB: {dob}
     ➤ Gender: {gender}
     ➤ Race: {race}
     ➤ Sexual Orientation: {sexual_orientation}
     ➤ Religion: {religion}
     ➤ Language: {language}

╚───────────────────────────────────────────────────────╝



                     PERSONAL INFO
╔───────────────────────────────────────────────────────╗
     ➤ IP: {ip}
     ➤ ISP: {isp}
     ➤ SSN: {ssn}
     ➤ Area Code: {area_code}
     ➤ Current Address: {current_address}
       ➣ Previous Address: {previous_address1}
     ➤ Phone Number: {phone_number} 

       ADDITIONAL INFORMATION
       ➣ Username: {username}
       ➣ Aliases: {aliases}
       ➣ Emails: {emails}
       ➣ Password: {passwords}
       ➣ Instagram: {instagram}
       ➣ Snapchat: {snapchat}
       ➣ Twitter: {twitter}
       ➣ Discord: {discord}

╚───────────────────────────────────────────────────────╝



                      FAMILY INFO
╔───────────────────────────────────────────────────────╗
     ➤ Mothers Name: {mother_name}
     ➤ Mothers Age: {mother_age}
     ➤ Mothers DOB: {mother_dob}
     ➤ Mothers Number: {mother_number} 
     ➤ Mothers Address: {mother_address}
     ➤ Mothers SSN: {mother_ssn}    

       ADDITIONAL INFORMATION
       ➣ Mothers Emails: {mother_emails}
       ➣ Mothers Passwords: {mother_passwords}
       ➣ Mothers Instagram: {mother_instagram}
       ➣ Mothers Facebook: {mother_facebook}
       ➣ Mothers Twitter: {mother_twitter}
       ➣ Mothers LinkedIn: {mother_linkedin}

     ➤ Fathers Name: {father_name}
     ➤ Fathers Age: {father_age}
     ➤ Fathers DOB: {father_dob}
     ➤ Fathers Number: {father_number} 
     ➤ Fathers Address: {father_address}
     ➤ Fathers SSN: {father_ssn}   

       ADDITIONAL INFORMATION
       ➣ Fathers Emails: {father_emails}
       ➣ Fathers Passwords: {father_passwords}
       ➣ Fathers Instagram: {father_instagram}
       ➣ Fathers Facebook: {father_facebook}
       ➣ Fathers Twitter: {father_twitter}
       ➣ Fathers LinkedIn: {father_linkedin}

╚───────────────────────────────────────────────────────╝
    '''


def questions():
    print("after you fill in all the information, the dox will be saved in /results/doxes")
    reason = input("Reason of the dox:")
    print("If you dont have their info just press enter")
    name = input("Name:")
    age = input("Age:")
    dob = input("DOB:")
    gender = input("Gender:")
    race = input("Race:")
    sexual_orientation = input("Sexual Orientation:")
    religion = input("Religion:")
    language = input("Language:")
    ip = input("IP:")
    isp = input("ISP:")
    ssn = input("SSN:")
    area_code = input("Area Code:")
    current_address = input("Current Address:")
    previous_address1 = input("Previous Address:")
    phone_number = input("Phone Number:")
    username = input("Username:")
    alias = input("Aliases:").split(", ")
    emails = input("Emails:")
    passwords = input("Passwords:")
    instagram = input("Instagram:")
    snapchat = input("Snapchat:")
    twitter = input("Twitter:")
    discord = input("Discord (you should do username:userid):")
    print("You will now be entering their family info, their mother and fathers shit")
    mother_name = input("Mothers Name:")
    mother_age = input("Mothers Age:")
    mother_dob = input("Mothers DOB:")
    mother_number = input("Mothers Number:")
    mother_address = input("Mothers Address:")
    mother_ssn = input("Mothers SSN:")
    mother_emails = input("Mothers Emails:")
    mother_passwords = input("Mothers Passwords:")
    mother_instagram = input("Mothers Instagram:")
    mother_facebook = input("Mothers Facebook:")
    mother_twitter = input("Mothers Twitter:")
    mother_linkedin = input("Mothers LinkedIn:")
    father_name = input("Fathers Name:")
    father_age = input("Fathers Age:")
    father_dob = input("Fathers DOB:")
    father_number = input("Fathers Number:")
    father_address = input("Fathers Address:")
    father_ssn = input("Fathers SSN:")
    father_emails = input("Fathers Emails:")
    father_passwords = input("Fathers Passwords:")
    father_instagram = input("Fathers Instagram:")
    father_facebook = input("Fathers Facebook:")
    father_twitter = input("Fathers Twitter:")
    father_linkedin = input("Fathers LinkedIn:")
    return dox(reason, name, username, alias, current_address, previous_address1, ip, isp, area_code, phone_number, emails, passwords, language, dob, age, race, gender, sexual_orientation, religion, ssn, discord, instagram, twitter, snapchat, mother_name, mother_age, mother_dob, mother_number, mother_address, mother_emails, mother_passwords, mother_ssn, mother_facebook, mother_linkedin, mother_instagram, mother_twitter, father_name, father_dob, father_age, father_number, father_address, father_emails, father_passwords, father_ssn, father_facebook, father_linkedin, father_instagram, father_twitter)