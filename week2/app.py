import json
import os
def write_kar_js(name,email,city,degree,field,skill_name,skill_level,score):
    try:
        name=input("enter full name :").strip()
        email=input("enter email : ").strip()
        city=input("enter your city: ").strip()
        degree = input("Degree: ")
        field = input("Field: ")
        skill_name = input("Skill: ")
        skill_level = input("Skill level: ")
        score = int(input("Skill score: "))
        karvands={
            "name":name,
            "email":email,
            "city":city,
            "educatoin":{
                "degree":degree,
                "filed":field
                },
            "skill":[
                {
                    "skill_name":skill_name,
                    "skill_level":skill_level,
                    "scor":score
                    }
                ]

            

        }
        with open("data/karvand.json","w",encoding="utf-8") as f:
            json.dump(karvands, f, ensure_ascii=False, indent=4)
    except json.JSONDecodeError:
        print("")
            
   



while True:
    menu=input(
               """enter one of the options\n
               add_karvand\n
               show_karvand\nedite_karvand\n
               deiet_karvand\nreport\nexit"""
               )
    try:
        if 