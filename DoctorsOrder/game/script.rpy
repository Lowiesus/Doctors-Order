﻿# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")
define doctor_sycamore = Character("Doctor Sycamore")
define announcer = Character("Announcer")
define patient = Character("Patient")
define you = Character("You")
# image for doctor sycamoer
image sycamore smiling = "doctor_sycamore.png"

#image for the patient
image patient neutral ="patient neutral.png"
image patient happy = "patient happy.png"
image patient sad = "patient sad.png"
image patient teary = "patient teary.png"
image patient neutral talk = "patient neutral talk.png"
image patient happy talk = "patient happy talk.png"
image patient sad talk = "patient sad talk.png"
image patient teary talk = "patient teary talk.png"

# background images scenes
image clinic = "clinic.jpg"
image emergency = "emergency.png"
image hospital = "hospital.png"
image office = "office.jpg"


# Transformations for doctor sycamore's image

transform sycamore_small:
    zoom 0.5
    xalign 1
    yalign 0.5

# background images settings
transform clinic_default:
    zoom 2.5
    xalign 0.5
    yalign 0.0

transform hospital_default:
    zoom 1.0

transform emergency_default:
    zoom 1.6

transform clinic_clinic_default:
    zoom 1.5


# The game starts here.

label start:

    # Scene: Loading Screen
    label hints:
        scene hospital at hospital_default
        "Butot balat lumilipad"

        scene hospital at hospital_default

        "You are a new resident doctor in Skidi Toilet Hospital."

# Scene: Welcome Screen
label welcome_screen: 
    scene office at clinic_default
    with fade

    play music "background music.mp3" volume 0.1

    show sycamore smiling at sycamore_small, right

    # line 1
    doctor_sycamore "Welcome aboard, doc! I'm Doctor Sycamore, and I’ll be your guide through our protocols, ensuring that our response is always swift and effective."

    # line 2
    doctor_sycamore "It’s going to be intense — but don’t worry. We’ve got each other’s backs. You’ll learn quickly, just stay sharp, breathe, and do your best."

    # line 3
    doctor_sycamore "First, we’ll walk through some essential protocols. These will help us remain professional within the hospital and ensure our patients’ safety."

    # line 4
    doctor_sycamore "Let’s start with patient information."

    # line 5
    doctor_sycamore "It’s our protocol to collect each patient’s personal details, strictly for medical purposes only."

    # line 6
    doctor_sycamore "Using someone’s personal information outside of the hospital is a serious offense. Always ensure this data stays within hospital use and strictly for healthcare needs."

    # line 7
    doctor_sycamore "Next, we need to check if the patient has had any prior medical procedures. Understanding their medical history helps us plan the most effective treatment."

    # line 8
    doctor_sycamore "If there’s been a past operation, we’ll need specific details — including the procedure and the medical personnel involved."

    # line 9
    doctor_sycamore "Lastly, treat every patient with care and compassion."

    # line 10
    doctor_sycamore "Whenever possible, encourage them to consult with a doctor and ensure they feel supported throughout their treatment."

    # line 10 - 1
    doctor_sycamore "We must also do our best to avoid making patients feel anxious."
    doctor_sycamore "Deliver news in a calm and friendly manner — this helps ease their worries and builds trust."

    hide sycamore smiling
    stop music fadeout 1.0

    scene emergency at emergency_default
    with fade

    play music "buzzer.mp3" volume 0.1

    # line 11
    announcer "*BZZT!! BZZT!!* Attention: A patient has arrived with a possible knee injury. Any available doctors, please report to the emergency room! *BZZT!! BZZT!!*"

    # line 12
    stop music fadeout 1.0

    scene office at clinic_default
    with fade

    play music "background music.mp3" volume 0.1

    show sycamore smiling at sycamore_small, right
    doctor_sycamore "Well, doctor — duty calls. Let’s get moving and head to the emergency room."



# Scene 1: Patient’s Arrival
label patient_arrival:
    scene emergency at emergency_default
    with fade

    show patient neutral at sycamore_small, left 

    "A teenager arrives at the hospital with a knee injury from a soccer game."
    "They appear nervous as they sit in the waiting area."

    hide patient neutral

    menu:
        "How do you approach the patient?"
        "Hi, my name is Doctor Jest. You’re in good hands — we’ll do our best to take care of you. Can you tell me what happened to your knee? Have you had any previous medical treatments we should know about?":
            jump answer_confident_scene_1
        "What happened to your knee?":
            jump answer_neutral_scene_1
        "Ermm... your knee looks bad. What happened?":
            jump answer_anxious_scene_1

label answer_anxious_scene_1:
    show patient teary at sycamore_small, left

    "The patient responds with a guarded and anxious tone."
    hide patient teary
    show patient teary talk at sycamore_small, left

    patient "Uhm... it happened during a game. It hurts a lot..."

    "He shifts uncomfortably, visibly more anxious."

    patient "The pain got worse so I asked my coach to bring me here."

    hide patient teary
    show patient teary at sycamore_small, left

    you "I see... did anything else happen?"

    "He avoids eye contact and speaks with hesitation."

    hide patient teary
    show patient teary talk at sycamore_small, left

    patient "No... nothing else happened..."

    hide patient teary
    show patient teary at sycamore_small, left

    you "Okay. Before we proceed, what's your name? How old are you, and who are your guardians?"

    hide patient teary
    show patient teary talk at sycamore_small, left

    patient "My name is Steven Nicholas. I'm 18 years old, and my dad is my coach. You can just ask him the rest..."

    hide patient teary
    show patient teary at sycamore_small, left

    you "Alright, thank you. I’ll take you to the diagnostic room now so we can run some tests."

    jump diagnostics

label answer_neutral_scene_1:
    show patient sad at sycamore_small, left

    "The patient seems a little uneasy. A warmer tone might have helped."

    hide patient sad
    show patient sad talk at sycamore_small, left

    patient "I got injured during a soccer game... it's been hurting since then."

    "He speaks with a flat, quiet tone."

    patient "It started hurting more, so I told my coach to bring me here."

    hide patient sad
    show patient sad at sycamore_small, left

    you "Don’t worry, we’ll take care of you as soon as we get the information we need."

    you "What's your name? How old are you? And who are your guardians?"

    hide patient sad
    show patient sad talk at sycamore_small, left

    patient "My name is Steven Nicholas. I’m 18. My dad is my coach — he can give you more info if you need."

    hide patient sad
    show patient sad at sycamore_small, left

    you "Thanks, Steven. I’ll bring you to the diagnostic room now so we can begin the tests."

    jump diagnostics

label answer_confident_scene_1:
    show patient happy at sycamore_small, left

    "The patient smiles slightly, reassured by your calm and professional tone."

    hide patient happy
    show patient happy talk at sycamore_small, left

    patient "Thanks, Doctor. I hurt my knee during soccer. I didn’t have surgery before, but I did sprain it last year."

    "He seems more open and relaxed."

    patient "At first I thought it was just a sprain, but the pain got worse. That’s why my coach brought me here."

    hide patient happy
    show patient happy at sycamore_small, left

    you "Don’t worry — we’ll get you fixed up in no time. You’ll be back on the field soon enough!"

    hide patient happy
    show patient happy talk at sycamore_small, left

    patient "Thank you so much, Doc! I trust you completely."

    hide patient happy
    show patient happy at sycamore_small, left

    you "You're welcome, Steven. First, I need to gather a few details, then we’ll get you into the diagnostic room."

    you "What’s your full name, your age, and who’s your guardian?"

    hide patient happy
    show patient happy talk at sycamore_small, left

    patient "My name is Steven Nicholas. I'm 18, and my dad is my coach. He can help with the rest if needed."

    hide patient happy
    show patient happy at sycamore_small, left

    you "Perfect. Thanks, Steven. Let’s head to diagnostics and run some tests."

    jump diagnostics

    # Scene 2: Diagnostic Process - Performing Tests
    label diagnostics:
    scene clinic at clinic_clinic_default
    with fade
    "You move the patient to the examination room and gently help him onto the bed. His leg is slightly swollen."
    "You kneel beside him, observing the injured knee closely—there’s bruising and limited range of motion."

    menu:
        "What do you say while performing the diagnostic?"
        "I’ll be checking your knee, let me know if anything hurts, okay?":
            jump answer_confident_scene_2
        "We need an X-ray to see inside the knee and check for tearing or fractures.":
            jump answer_neutral_scene_2
        "We will proceed to do some tests. You’ll find out soon enough.":
            jump answer_anxious_scene_2

label answer_confident_scene_2:
    show patient happy at sycamore_small, left
    "You place a hand gently on Steven’s leg and begin the examination."
    "He flinches slightly as you press around the joint, but your calm presence seems to help."
    hide patient happy
    show patient happy talk at sycamore_small, left
    patient "Alright, Doctor. I’ll let you know if anything feels painful."
    hide patient happy talk
    show patient neutral at sycamore_small, left
    "He watches you with growing trust."
    "You finish the physical assessment and wheel in the portable X-ray machine."
    jump diagnosis_result

label answer_neutral_scene_2:
    show patient sad at sycamore_small, left
    "You begin examining the leg, then prepare the X-ray plates."
    "Steven doesn’t say much but watches you with unease."
    hide patient sad
    show patient sad talk at sycamore_small, left
    patient "Okay... if you say so. I just hope it's not too bad."

    hide patient sad talk

    show patient neutral at sycamore_small, left
    "You nod and proceed with the imaging process, noting his guarded body language."
    jump diagnosis_result

label answer_anxious_scene_2:
    show patient teary at sycamore_small, left
    "You move efficiently but offer no clear context for the tests."
    "Steven tenses up and glances at the door."
    hide patient teary
    show patient teary talk at sycamore_small, left
    patient "Wait... what kind of tests? Is it serious?"
    "He grips the edge of the bed tightly, clearly unnerved by your tone."

    hide patient teary talk
    "You silently position the X-ray machine and begin the scan."
    jump diagnosis_result

    # Scene 3: Diagnosis Confirmation
    label diagnosis_result:
    scene clinic at clinic_clinic_default
    with fade
    "You review the results from the X-ray. The image clearly shows a transverse fracture across the kneecap."
    "Steven sits up on the bed, watching you anxiously from across the room."

    menu:
        "How do you deliver the news?"
        "Your knee has a fracture – which is treatable, and don’t worry! We’ll walk you through every step of the operation.":
            jump answer_confident_scene_3
        "You’ll need surgery to fix your knee. It's common and you’ll surely recover.":
            jump answer_neutral_scene_3
        "Dang, your knee is broken. We’ll have to operate on it.":
            jump answer_anxious_scene_3

label answer_confident_scene_3:
    show patient happy at sycamore_small, left
    "You pull up a stool beside him and show the X-ray results gently."
    "Your voice is calm and steady, explaining the injury and the next steps clearly."
    hide patient happy
    show patient happy talk at sycamore_small, left
    patient "Thank you, Doctor. I was really nervous, but you make it sound manageable."
    "He smiles weakly, but you can see relief in his eyes."
    "You nod and begin discussing surgery preparation."
    jump surgery_prep

label answer_neutral_scene_3:
    show patient sad at sycamore_small, left
    "You stand beside the monitor, pointing out the fracture without much inflection."
    "Steven blinks a few times and slowly nods."
    hide patient sad
    show patient sad talk at sycamore_small, left
    patient "Okay... I guess if it’s necessary. Just tell me what I have to do."
    "He glances at the X-ray again, still worried."
    "You hand him a consent form and explain the next steps."
    jump surgery_prep
#mlem 
label answer_anxious_scene_3:
    show patient teary at sycamore_small, left
    "You casually toss the X-ray onto the nearby table and shrug."
    hide patient teary
    show patient teary talk at sycamore_small, left
    patient "Wait, what?! Surgery?! That sounds really serious..."
    "His breathing grows shallow, panic creeping into his expression."
    "You realize you may have startled him unnecessarily."
    jump surgery_prep

    # Scene 4: Surgical Preparation - Minigame Style
    label surgery_prep:
        scene operating_room
        "You begin the surgery on the kneecap fracture."

    # Step 1
    label step1:
        "Step 1: Preparing the knee"
        menu:
            "Choose the correct action:"
            "Sterilize the knee using antiseptic.":
                jump step2
            "Mark the knee for the incision.":
                "You need to sterilize the knee first."
                jump step1
            "Cut the skin of the knee.":
                "That’s too early! The area isn’t even sterile."
                jump step1

    # Step 2
    label step2:
        "Step 2: What’s next?"
        menu:
            "Choose the correct action:"
            "Mark the knee for the incision":
                jump step3
            "Tap the knee with a hammer":
                "That’s not appropriate!"
                jump step2
            "Cut the skin of the knee":
                "Marking is required before cutting."
                jump step2

    # Step 3
    label step3:
        "Step 3: What’s next?"
        menu:
            "Choose the correct action:"
            "Apply anesthesia":
                jump step4
            "Bend the knee":
                "That’s unnecessary here."
                jump step3
            "Apply for college":
                "Now’s not the time for that!"
                jump step3

    # Step 4
    label step4:
        "Step 4: What’s next?"
        menu:
            "Choose the correct action:"
            "Put an incision where the mark is":
                jump step5
            "Put an incision next the mark":
                "You must be precise."
                jump step4
            "Put an incision above the mark":
                "Not accurate!"
                jump step4

    # Step 5
    label step5:
        "Step 5: What’s next?"
        menu:
            "Choose the correct action:"
            "Use surgical clamps to hold the skin.":
                jump step6
            "Hit the bone with a hammer.":
                "That would be very harmful."
                jump step5
            "Use the saw to remove the fractured bone.":
                "Too early to do this."
                jump step5

    # Step 6
    label step6:
        "Step 6: What’s next?"
        menu:
            "Choose the correct action:"
            "Use a drill to put holes on the bone where the screws, wires, metal plates will be placed.":
                jump step7
            "Close the wound with clamps and stitch it back closed.":
                "You're not done yet!"
                jump step6
            "Remove the fractured bone and replace it with a prosthetic kneecap.":
                "That's not needed in this case."
                jump step6

    # Step 7
    label step7:
        "Step 7: What’s next?"
        menu:
            "Choose the correct action:"
            "Use metal plates and wires to put the fractured kneecap back in place.":
                jump step8
            "Use prosthetic kneecaps to replace the fractured one.":
                "That’s not necessary for this injury."
                jump step7
            "Use a hammer to break away the rest of the broken bones.":
                "No! That would worsen the injury."
                jump step7

    # Step 8
    label step8:
        "Final Step: What’s next?"
        menu:
            "Choose the correct action:"
            "Remove the clamps of the skin and stitch the wound closed.":
                jump recovery
            "Hammer the metal plates and screws to make sure they’re sturdy.":
                "No need to hammer them in."
                jump step8
            "Clean the bone using isopropyl alcohol to make sure the metal plates and screws are clean.":
                "It’s too late for that now."
                jump step8
    # Scene 5: Monitoring Recovery
    label recovery:
        scene recovery_room
        "You completed the surgery successfully."

        menu:
            "How do you inform the patient?"
            "Good news! The surgery was a success! I’ll prescribe meds and schedule physical therapy.":
                jump maintenance
            "We fixed your knee, you’ll only partially be unable to walk.":
                "Patient nods, a bit unsure."
                jump maintenance
            "I will be discharging you now.":
                "Patient seems confused and concerned."
                jump maintenance

    # Scene 6: Maintenance
    label maintenance:
        scene discharge_room
        "You’re about to discharge the patient. Give final instructions."

        menu:
            "Before discharge..."
            "Before I discharge you, here are some friendly reminders...":
                "You give a detailed explanation of the medication and activities to avoid."
                "The patient smiles, feeling cared for."
                jump ending
            "Don’t do any heavy work and take your medications.":
                "The patient nods, unsure of the details."
                jump ending
            "You’ve been discharged, you can leave now.":
                "The patient leaves without knowing the full care routine."

    label ending:
        scene black
        "Thank you for playing Doctor's Order: Emergency Room Edition!"

    return
