#!/usr/bin/python3




list1 = {"all": [{"First":"Askia","Last":"Wingfield","Skill Level":"astonishing","Spirit Animal":"lion","Super Power":"Regenerative Healing Factor"},{"First":"Chen","Last":"Xin","Skill Level":"awe-inspiring","Spirit Animal":"porcupine","Super Power":"Adoptive Muscle Memory"},{"First":"Everett","Last":"Strunk","Skill Level":"breathtaking","Spirit Animal":"mandrill","Super Power":"Body Part Substitution"},{"First":"Jacob","Last":"Roe","Skill Level":"fearsome","Spirit Animal":"guinea pig","Super Power":"Anatomical Liberation"},{"First":"Josh","Last":"Ayala","Skill Level":"formidable","Spirit Animal":"camel","Super Power":"Additional Limbs"},{"First":"Kevin","Last":"Martinez","Skill Level":"imposing","Spirit Animal":"panther","Super Power":"Organic Constructs"},{"First":"Luke","Last":"Thompson","Skill Level":"impressive","Spirit Animal":"coati","Super Power":"Deflection"},{"First":"Marco","Last":"Santos","Skill Level":"magnificent","Spirit Animal":"bumblebee","Super Power":"Replication"},{"First":"Michael","Last":"Williams","Skill Level":"overwhelming","Spirit Animal":"fish","Super Power":"Invisibility"},{"First":"Mike","Last":"Wright","Skill Level":"stunning","Spirit Animal":"mink","Super Power":"Needle Projection"},{"First":"Oscar","Last":"Abalos","Skill Level":"wondrous","Spirit Animal":"ermine","Super Power":"Immobility"},{"First":"Ryan","Last":"Larson","Skill Level":"grand","Spirit Animal":"marmoset","Super Power":"Camouflage"},{"First":"Shirley","Last":"Wu","Skill Level":"mind-blowing","Spirit Animal":"koala","Super Power":"Self-Detonation"}]}


#count = 0

for count in range(0,13):

    firstname = list1['all'][count]['First']
    lastname = list1['all'][count]['Last']
    spirit = list1['all'][count]['Spirit Animal']
    skillz = list1['all'][count]['Skill Level']
    power = list1['all'][count]['Super Power']


    print(f"""
    Name: {firstname} {lastname}
    Skill Level: {skillz}
    Spirit Animal: {spirit}
    Super Power: {power}
    """)
    print("-------------------------------")

    #print(x['First'])
    #print(x['Last'])
    #print(x['Spirit Animal'])
    #print(x['Super Power'])
    





#print(f'Name: {firstname}')
#print(f'Skill Level: {skillz}')
#print(f'Spirit Animal: {spirit}')
#print(f'Super Power: {power}')

#else:
    #break




#print(f'My name is {firstname} and my spirit animal is a {spirit}!')



