# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
# mlemmers

define doctor_sycamore = Character("Doctor Sycamore", who_color="#4fb6a7")
define announcer = Character("Announcer", who_you = "#dff300")
define patient = Character("Patient", who_color = "#c84b4b")
define you = Character("You", who_color = "#ea0d7f")
# image for doctor sycamoer
image doctor writing talk = "doctor writing talk.png"
image doctor happy = "doctor happy.png"
image doctor talk = "doctor talk.png"
image doctor smile = "doctor smile.png"
image doctor happy talk = "doctor happy talk.png"
image doctor writing = "doctor writing.png"
image doctor embarassed = "doctor embarassed.png"
image doctor disappoint = "doctor disappoint.png"
image doctor close = "doctor close.png"
image doctor talking = "doctor talking.png"

#image for the patient
image patient neutral ="patient neutral.png"
image patient happy = "patient happy.png"
image patient sad = "patient sad.png"
image patient teary = "patient teary.png"
image patient neutral talk = "patient neutral talk.png"
image patient happy talk = "patient happy talk.png"
image patient sad talk = "patient sad talk.png"
image patient teary talk = "patient teary talk.png"
image patient neutral looking="patient neutral look.png"
image patient happy looking = "patient happy look.png"
image patient sad looking = "patient sad look.png"
image patient teary looking = "patient teary look.png"
image patient neutral talk looking = "patient neutral talklook .png"
image patient happy talk looking = "patient happy talk look.png"
image patient sad talk looking = "patient sad talk look.png"
image patient teary talk looking = "patient teary talk look.png"

image overlay positive answer = "8.png"
image overlay neutral answer = "9.png"
image overlay negative answer = "10.png"

image knee = "knee.png"
image knee focus = "knee focus.png"
image knee betadine = "knee betadine.png"
image knee inject = "knee inject.png"
image knee open = "knee open.png"
image knee hole = "knee hole.png"
image knee bracket = "knee bone bracket.png"
image knee dashline = "knee dash line.png"
image knee closed = "knee closed.png"
image knee stitched = "knee stitched.png"


# background images scenes
image clinic = "clinic.png"
image emergency = "emergency.png"
image hospital = "hospital.png"
image office = "office.jpg"
image operating table = "green_background.jpg"


# Transformations for doctor images
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
    zoom 2.0

transform emergency_default:
    zoom 1.6

transform clinic_clinic_default:
    zoom 1.0

transform operating_default:
    zoom 2.7
    yalign 4
    xalign 0.5

transform knee_default:
    zoom 0.8
    xalign 0.5
    yalign 0.5

transform knee_single:
    zoom 1.0
    xalign 0.5
    yalign 0.5

transform knee_single_default:
    zoom 1.0
    xalign 0.5
    yalign 0.5

transform overlay:
    zoom 0.2
    xalign 1.0
    yalign -0.0

#Variable goes here
default trust_points = 0
default confidence_points = 0

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

    show doctor talk at sycamore_small, right

    # line 1
    doctor_sycamore "Welcome aboard, doc! I'm Doctor Sycamore, and I’ll be your guide through our protocols, ensuring that our response is always swift and effective."

    # line 2
    doctor_sycamore "It’s going to be intense — but don’t worry. We’ve got each other’s backs. You’ll learn quickly, just stay sharp, breathe, and do your best."

    # line 3
    doctor_sycamore "First, we’ll walk through some essential protocols. These will help us remain professional within the hospital and ensure our patients’ safety."

    hide doctor talk
    show doctor smile at sycamore_small, right
    # line 4
    doctor_sycamore "Let’s start with patient information."
    hide doctor smile
    show doctor happy talk  at sycamore_small, right
    # line 5
    doctor_sycamore "It’s our protocol to collect each patient’s personal details, strictly for medical purposes only."

    # line 6
    doctor_sycamore "Using someone’s personal information outside of the hospital is a serious offense. Always ensure this data stays within hospital use and strictly for healthcare needs."
    hide doctor happy talk
    show doctor talk at sycamore_small, right
    # line 7
    doctor_sycamore "Next, we need to check if the patient has had any prior medical procedures. Understanding their medical history helps us plan the most effective treatment."

    # line 8
    doctor_sycamore "If there’s been a past operation, we’ll need specific details — including the procedure and the medical personnel involved."

    hide doctor happy talk
    show doctor happy at sycamore_small, right
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

    show doctor happy talk at sycamore_small, right
    doctor_sycamore "Well, doctor — duty calls. Let’s get moving and head to the emergency room."



# Scene 1: Patient’s Arrival
label patient_arrival:
    scene emergency at emergency_default
    with fade

    show patient teary looking at sycamore_small, left

    "A teenager arrives at the hospital with a knee injury from a soccer game."
    "They appear nervous as they sit in the waiting area."

    hide patient teary looking

    menu:
        "How do you approach the patient?"
        "Hi, my name is Doctor Jest. You’re in good hands — we’ll do our best to take care of you. Can you tell me what happened to your knee? Have you had any previous medical treatments we should know about?":
            $ trust_points += 1
            $ confidence_points += 1
            show overlay positive answer at overlay with dissolve
            pause 1
            hide overlay positive answer with dissolve
            jump answer_confident_scene_1
        "What happened to your knee?":
            $ trust_points += 0
            $ confidence_points += 1
            show overlay neutral answer at overlay with dissolve
            pause 1
            hide overlay neutral answer with dissolve
            jump answer_neutral_scene_1
        "Ermm... your knee looks bad. What happened?":
            $ trust_points += 0
            $ confidence_points += 0
            show overlay negative answer at overlay with dissolve
            pause 1
            hide overlay negative answer with dissolve
            jump answer_anxious_scene_1

label answer_anxious_scene_1:
    show patient teary looking at sycamore_small, left

    "The patient responds with a guarded and anxious tone."
    hide patient teary looking
    show patient teary talk looking at sycamore_small, left

    patient "Uhm... it happened during a game. It hurts a lot..."

    "He shifts uncomfortably, visibly more anxious."

    patient "The pain got worse so I asked my coach to bring me here."

    hide patient teary looking
    show patient teary looking at sycamore_small, left

    you "I see... did anything else happen?"

    "He avoids eye contact and speaks with hesitation."

    hide patient teary looking
    show patient teary talk looking at sycamore_small, left

    patient "No... nothing else happened..."

    hide patient teary looking
    show patient teary looking at sycamore_small, left

    you "Okay. Before we proceed, what's your name? How old are you, and who are your guardians?"

    hide patient teary looking
    show patient teary talk looking at sycamore_small, left

    patient "My name is Steven Nicholas. I'm 18 years old, and my dad is my coach. You can just ask him the rest..."

    hide patient teary looking
    show patient teary looking at sycamore_small, left

    you "Alright, thank you. I’ll take you to the diagnostic room now so we can run some tests."

    jump diagnostics

label answer_neutral_scene_1:
    show patient sad at sycamore_small, left

    "The patient seems a little uneasy. A warmer tone might have helped."

    hide patient sad looking
    show patient sad talk looking at sycamore_small, left

    patient "I got injured during a soccer game... it's been hurting since then."

    "He speaks with a flat, quiet tone."

    patient "It started hurting more, so I told my coach to bring me here."

    hide patient sad looking
    show patient sad looking at sycamore_small, left

    you "Don’t worry, we’ll take care of you as soon as we get the information we need."

    you "What's your name? How old are you? And who are your guardians?"

    hide patient sad looking
    show patient sad talk looking at sycamore_small, left

    patient "My name is Steven Nicholas. I’m 18. My dad is my coach — he can give you more info if you need."

    hide patient sad looking
    show patient sad looking at sycamore_small, left

    you "Thanks, Steven. I’ll bring you to the diagnostic room now so we can begin the tests."

    jump diagnostics

label answer_confident_scene_1:
    show patient happy at sycamore_small, left

    "The patient smiles slightly, reassured by your calm and professional tone."

    hide patient happy looking
    show patient happy talk looking at sycamore_small, left

    patient "Thanks, Doctor. I hurt my knee during soccer. I didn’t have surgery before, but I did sprain it last year."

    "He seems more open and relaxed."

    patient "At first I thought it was just a sprain, but the pain got worse. That’s why my coach brought me here."

    hide patient happy looking
    show patient happy looking at sycamore_small, left

    you "Don’t worry — we’ll get you fixed up in no time. You’ll be back on the field soon enough!"

    hide patient happy looking
    show patient happy talk looking at sycamore_small, left

    patient "Thank you so much, Doc! I trust you completely."

    hide patient happy looking
    show patient happy looking at sycamore_small, left

    you "You're welcome, Steven. First, I need to gather a few details, then we’ll get you into the diagnostic room."

    you "What’s your full name, your age, and who’s your guardian?"

    hide patient happy looking
    show patient happy talk looking at sycamore_small, left

    patient "My name is Steven Nicholas. I'm 18, and my dad is my coach. He can help with the rest if needed."

    hide patient happy looking
    show patient happy looking at sycamore_small, left

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
            $ trust_points += 1
            $ confidence_points += 1
            show overlay positive answer at overlay with dissolve
            pause 1
            hide overlay positive answer with dissolve
            jump answer_confident_scene_2
        "We need an X-ray to see inside the knee and check for tearing or fractures.":
            $ trust_points += 0
            $ confidence_points += 1
            show overlay neutral answer at overlay with dissolve
            pause 1
            hide overlay neutral answer with dissolve
            jump answer_neutral_scene_2
        "We will proceed to do some tests. You’ll find out soon enough.":
            $ trust_points += 0
            $ confidence_points += 0
            show overlay negative answer at overlay with dissolve
            pause 1
            hide overlay negative answer with dissolve
            jump answer_anxious_scene_2

label answer_confident_scene_2:
    show patient happy looking at sycamore_small, left
    "You place a hand gently on Steven’s leg and begin the examination."
    "He flinches slightly as you press around the joint, but your calm presence seems to help."
    hide patient happy looking
    show patient happy talk looking at sycamore_small, left
    patient "Alright, Doctor. I’ll let you know if anything feels painful."
    hide patient happy talk looking
    show patient neutral looking at sycamore_small, left
    "He watches you with growing trust."
    "You finish the physical assessment and wheel in the portable X-ray machine."
    jump diagnosis_result

label answer_neutral_scene_2:
    show patient sad looking at sycamore_small, left
    "You begin examining the leg, then prepare the X-ray plates."
    "Steven doesn’t say much but watches you with unease."
    hide patient sad looking
    show patient sad talk looking at sycamore_small, left
    patient "Okay... if you say so. I just hope it's not too bad."

    hide patient sad talk looking

    show patient neutral looking at sycamore_small, left
    "You nod and proceed with the imaging process, noting his guarded body language."
    jump diagnosis_result

label answer_anxious_scene_2:
    show patient teary looking at sycamore_small, left
    "You move efficiently but offer no clear context for the tests."
    "Steven tenses up and glances at the door."
    hide patient teary looking
    show patient teary talk looking at sycamore_small, left
    patient "Wait... what kind of tests? Is it serious?"
    "He grips the edge of the bed tightly, clearly unnerved by your tone."

    hide patient teary talk looking
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
            $ trust_points += 1
            $ confidence_points += 1
            show overlay positive answer at overlay with dissolve
            pause 1
            hide overlay positive answer with dissolve
            jump answer_confident_scene_3
        "You’ll need surgery to fix your knee. It's common and you’ll surely recover.":
            $ trust_points += 0
            $ confidence_points += 1
            show overlay neutral answer at overlay with dissolve
            pause 1
            hide overlay neutral answer with dissolve
            jump answer_neutral_scene_3
        "Dang, your knee is broken. We’ll have to operate on it.":
            $ trust_points += 0
            $ confidence_points += 0
            show overlay negative answer at overlay with dissolve
            pause 1
            hide overlay negative answer with dissolve
            jump answer_anxious_scene_3

label answer_confident_scene_3:
    show patient happy looking at sycamore_small, left
    "You pull up a stool beside him and gently show the X-ray results."
    "Your voice is calm and steady as you explain the injury and the next steps clearly."
    
    hide patient happy looking
    show patient happy talk looking at sycamore_small, left
    patient "Thank you, Doctor. I was really nervous, but the way you explain it makes it feel manageable."
    
    "He smiles weakly, but you can see the relief in his eyes."
    
    hide patient happy looking
    show patient neutral looking at sycamore_small, left
    
    "You nod and begin discussing the surgery preparation."
    
    you "Alright, before we proceed with the surgery, I'd like to introduce you to Doctor Sycamore."
    
    with fade
    show sycamore smiling at sycamore_small, right
    
    hide sycamore smilling

    show sycamore smilling at sycamore_small, right
    doctor_sycamore "Good day! I'm Doctor Sycamore, and I'll be assisting with your procedure. It's a pleasure to meet you."
    doctor_sycamore "We'll walk you through the entire process of repairing your leg, step by step."
    
    you "First, we'll begin with surgical preparation. We'll sanitize your leg and mark the area for the incision."
    
    you "Sanitizing is crucial to prevent any risk of infection."
    
    you "Next, we'll administer anesthesia to numb your leg. You won’t feel anything during the procedure—just a slight pinch from the injection."
    
    you "Finally, we'll stabilize your leg using medical-grade wires and screws. Don't worry, these are completely safe for your body."
    
    you "That would be all, if you have any questions please us know that we'll answer them for you."

    patient "Hmmmmmm... Nope, I have no questions anymore."

    doctor_sycamore "Alright! We'll notify you once the operation room is prepared and we will proceed to the medical procedure."

    jump surgery_prep


label answer_neutral_scene_3:
    show patient sad looking at sycamore_small, left
    "You stand beside the monitor, pointing out the fracture without much emotion."
    "Steven blinks a few times and slowly nods."
    
    hide patient sad looking
    show patient sad talk looking at sycamore_small, left
    
    patient "Okay... I guess if it’s necessary. Just tell me what I need to do."
    
    hide patient sad talk looking
    show patient sad looking at sycamore_small, left
    "He glances at the X-ray again, still looking worried."
    
    "You hand him a consent form and explain the next steps."
    
    you "Please sign this consent form before we proceed."
    
    "Steven signs the form, his expression still uncertain."
    
    you "Now, I'd like to introduce you to Doctor Sycamore. He'll be assisting me throughout your procedure."
    
    show sycamore smiling at sycamore_small, right
    with fade
    
    doctor_sycamore "Good day! I'm Doctor Sycamore, and I'll be helping with your procedure. It's a pleasure to meet you."
    
    patient "Nice to meet you, Doc! I'm Steven Nicholas."
    
    you "Now that you've signed the consent form, we'll begin preparing the operating room. We'll notify you when it's time to proceed."
    
    patient "Got it, Doc. Thanks!"
    
    jump surgery_prep


label answer_anxious_scene_3:
    show patient teary looking at sycamore_small, left
    "You casually toss the X-ray onto the nearby table and shrug."
    hide patient teary looking
    show patient teary talk looking at sycamore_small, left
    patient "Wait, what?! Surgery?! That sounds really serious..."

    "His breathing grows shallow, panic creeping into his expression."

    "You realize you may have startled him unnecessarily."

    you "We will be preparing the operation, please stay put. We will notify you once were ready for surgery."

    jump surgery_prep

    # Scene 4: Surgical Preparation - Minigame Style
    label surgery_prep:
        scene emergency at emergency_default
        "You have finished preparing the operating room and notified the patient to proceed to the the room."

        with fade
        show patient teary looking at sycamore_small, left
        patient "Alright, Doctor, we're ready to proceed with the surgery."
        
        you "Alright you can start changing clothes on the dressing room."
        you "Please wear this medical gown and then after that, you can laydown on the operating room and we will start the procedure"

        patient "Alright doc!"

        "You begin the surgery on the kneecap fracture."

    # Step 1
    hide patient teary looking
    scene green_background at operating_default
    with fade

    show knee at knee_default
    label step1:
        hide knee
        show knee at knee_single_default
        "Step 1: Preparing the knee"
        
        menu:
            "Choose the correct action:"
            "Sterilize the knee using antiseptic.":
                "We need to mark the incision first."
                jump step1
            "Mark the knee for the incision.":
                jump step2
            "Cut the skin of the knee.":
                "That’s too early! The area isn’t even sterile."
                jump step1

    # Step 2
    label step2:
        hide knee
        show knee dash line at knee_single with dissolve
        "Step 2: What’s next?"
        menu:
            "Choose the correct action:"
            "Sanitize the knee with betadine.":
                jump step3
            "Tap the knee with a hammer":
                "That’s not appropriate!"
                jump step2
            "Cut the skin of the knee":
                "Marking is required before cutting."
                jump step2

    # Step 3
    label step3:
        hide knee dash line
        show knee betadine at knee_single with dissolve
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
        hide knee dash line
        show knee inject at knee_single with dissolve
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
        hide knee inject
        show knee open at knee_single with dissolve
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
        hide knee open
        show knee open at knee_single with dissolve
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
    hide knee open
    show knee hole at knee_single with dissolve
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
    hide knee hole
    show knee bracket at knee_single with dissolve
    "Step 8: What’s next?"
    menu:
        "Choose the correct action:"
        "Remove the clamps holding the loose skin.":
            jump step9
        "Hammer the metal plates and screws to make sure they’re sturdy.":
            "No need to hammer them in."
            jump step8
        "Clean the bone using isopropyl alcohol to ensure the metal plates and screws are clean.":
            "It’s too late for that now."
            jump step8

# Step 9
label step9:
    hide knee bracket
    show knee closed at knee_single with dissolve
    "Step 9: What’s next?"
    menu:
        "Choose the correct action:"
        "Stitch the wound closed after removing the clamps.":
            jump step10
        "Hammer the metal plates and screws to make sure they’re sturdy.":
            "No need to hammer them in."
            jump step9
        "Clean the bone using isopropyl alcohol to ensure the metal plates and screws are clean.":
            "It’s too late for that now."
            jump step9

# Step 10
label step10:
    hide knee betadine
    show knee stitched at knee_single with dissolve
    "Step 10: What’s next?"
    menu:
        "Choose the correct action:"
        "Apply antiseptic and bandage the wound.":
            "The wound is now properly closed and protected."
            jump recovery
        "Hammer the metal plates and screws to make sure they’re sturdy.":
            "No need to hammer them in."
            jump step10
        "Clean the bone using isopropyl alcohol to ensure the metal plates and screws are clean.":
            "It’s too late for that now."
            jump step10

    # Scene 5: Monitoring Recovery
    label recovery:
    scene emergency at emergency_default
    "You completed the surgery successfully."

    "You approach the patient to inform them on how the surgery went."
    menu:
        "How do you inform the patient?"
        "Good news! The surgery was a success! I’ll prescribe meds and schedule physical therapy.":
            $ trust_points += 1
            $ confidence_points += 1
            show overlay positive answer at overlay with dissolve
            pause 1
            hide overlay positive answer with dissolve

            show patient happy look talk at sycamore_small
            patient "Oh, thank you so much, doctor! I was really worried, but this is such a relief."
            patient "When can I start physical therapy? I want to recover as soon as possible."
            hide patient happy look talk
            show patient happy look at sycamore_small

            "You smile reassuringly."

            you "Before we start therapy, we need to monitor your condition and ensure your knee is healing properly."
            you "For now, it's important to keep your leg elevated to reduce swelling and avoid putting weight on it."

            hide patient happy look
            show patient happy look talk at sycamore_small

            patient "That makes sense. How long will the monitoring last?"

            hide patient happy look talk
            show patient happy look at sycamore_small
            you "It depends on your healing progress, but within a few days, we can start light movement exercises."
            you "Once the swelling reduces and we confirm proper healing, we’ll gradually increase activity."
            
            hide patient happy look
            show patient happy look talk at sycamore_small

            patient "Alright, I’ll follow all the instructions. What else should I do to take care of my knee?"

            hide patient happy look talk
            show patient neutral look at sycamore_small
            you "Here are some key things to remember:"
            you "1. Keep your leg elevated above heart level, especially in the first few days."
            you "2. Apply ice packs for 15-20 minutes every few hours to minimize swelling."
            you "3. Take your prescribed pain medications as directed to manage discomfort."
            you "4. Avoid putting weight on your leg until your physical therapist clears you."
            you "5. Perform any recommended gentle exercises to prevent stiffness."

            hide patient happy look
            show patient happy look talk at sycamore_small
            patient "Got it! And when will I be able to walk normally again?"

            hide patient happy look talk
            show patient neutral look at sycamore_small
            you "That depends on how well your body heals, but with consistent therapy, most patients regain full mobility within a few months."

            hide patient neutral look
            show patient happy look talk at sycamore_small
            patient "Alright, I’ll do my best to stick to the recovery plan. Thank you, doctor!"

            hide patient happy look talk
            show patient happy look at sycamore_small
            "The patient nods, looking relieved and motivated to begin their recovery journey."

            jump ending

        "We fixed your knee, you’ll only partially be unable to walk.":
            $ trust_points += 1
            $ confidence_points += 0
            show overlay neutral answer at overlay with dissolve
            pause 1
            hide overlay neutral answer with dissolve
            
            show patient neutral look at sycamore_small
            "The patient looks at you with a confused expression."

            patient "Oh… okay. I mean, that’s good to hear, but could you clarify what you mean by ‘partially unable to walk’?"

            you "I mean that you’ll need crutches or a walker at first, and you should avoid putting full weight on your leg."
            you "Your mobility will be limited for a while, but physical therapy will help you regain full function."

            hide patient neutral look
            show patient neutral look talk at sycamore_small
            patient "I see. What do I need to do in the meantime to take care of my knee?"

            hide patient neutral look talk
            show patient neutral look at sycamore_small

            you "It’s important to keep your leg elevated and apply ice to reduce swelling."
            you "You’ll also need to wear a brace or a splint to protect the joint and avoid sudden movements."
            you "Most importantly, don’t try to walk without assistance until we confirm that your knee is strong enough."

            hide patient neutral look
            show patient neutral talk at sycamore_small
            patient "Okay, that’s good to know. How will I know if something is wrong with my knee?"

            hide patient neutral look talk
            show patient neutral look at sycamore_small
            you "Watch out for signs of complications, like increased swelling, severe pain, warmth, or redness."
            you "If you experience any of these symptoms, or if your leg feels numb, let us know immediately."

            hide patient neutral look
            show patient neutral look talk at sycamore_small
            patient "Alright, I’ll be careful and follow all the instructions. Thanks, doctor."

            hide patient neutral look talk
            show patient neutral look at sycamore_small
            "The patient still seems a bit uncertain but appreciates the clarification."

            you "Alright! That will be all. I will be seeing you soon for the general checkups."

            patient "Thanks Doc! I'll see you soon!"
            jump ending

        "I will be discharging you now.":
            $ trust_points += 0
            $ confidence_points += 0
            show overlay negative answer at overlay with dissolve
            pause 1
            hide overlay negative answer with dissolve

            show patient terrified look at sycamore_small
            patient "Wait… that’s it? I just had surgery, and now I’m being sent home?"
            patient "Are you sure it’s safe for me to leave already?"
            
            you "Actually, that was a mistake. You’re not ready for discharge yet."
            you "We need to monitor your recovery and make sure you understand how to take care of your knee before you go home."

            patient "Oh… okay. That makes more sense. What should I be doing to recover properly?"

            you "For now, focus on keeping your leg elevated, using ice to reduce swelling, and avoiding putting weight on it."
            you "We’ll also provide a brace or splint for support and start gentle exercises once it’s safe."
            you "I’ll also prescribe medication to manage pain and prevent blood clots."

            patient "That sounds more like what I expected. Thanks for explaining."

            "The patient looks slightly annoyed but relieved that they aren’t being sent home prematurely."

            jump ending

    # Scene 6: Maintenance
    label ending:
            scene office at clinic_default
            hide patient happy look
            if trust_points >= 3:  # Good Ending (3/4 or 4/4 trust points)
                jump good_ending

            elif trust_points == 2:  # Neutral Ending (2/4 trust points)
                jump neutral_ending

            else:  # Bad Ending (1/4 trust point)
                jump bad_ending

            label good_ending:
                scene office at clinic_default
            "You proceed to Doctor Sycamore's office to report and verify the case of the patient."
            "You knock on Doctor Sycamore's office door."

            doctor_sycamore "Come in!"

            "You step inside, and Doctor Sycamore looks up from his paperwork, smiling."

            show doctor happy at sycamore_small with dissolve

            doctor_sycamore "Welcome back, doc! And congratulations on your first successful operation!"

            doctor_sycamore "I just got the report and feedback from the patient about your care. Want to hear what they had to say?"

            you "Of course, doc! How did I do?"

            doctor_sycamore "You did great! Not only did you avoid making the patient anxious, but you also kept them well-informed about their treatment and recovery plan."

            doctor_sycamore "They were very happy with how everything was handled, and they feel much better already."

            you "That's really great to hear! I was hoping to make them feel as comfortable as possible."

            doctor_sycamore "And you did exactly that. Keep up this approach, and you’ll build strong trust with your future patients."

            "Doctor Sycamore pats you on the shoulder, clearly pleased with your performance."

            doctor_sycamore "This was just the first of many successful cases. Keep learning, keep improving, and you’ll go far."

            you "Thank you, doc. I won’t let you down!"

            "Feeling a sense of accomplishment, you leave the office with renewed confidence."

            label neutral_ending:
                scene office at clinic_default
            "You proceed to Doctor Sycamore's office to report and verify the case of the patient."
            "You knock on Doctor Sycamore's office door."

            doctor_sycamore "Come in!"

            "You step inside, and Doctor Sycamore gestures for you to sit."

            show doctor_sycamore at sycamore_small with dissolve
            doctor_sycamore "Welcome back, doc! Good job on successfully completing your first operation."

            doctor_sycamore "I’ve reviewed the patient’s feedback, and while you did well overall, there were a few areas that could have gone better."

            you "Oh? What do you mean?"

            doctor_sycamore "Well, the patient mentioned feeling a bit anxious during the post-op discussion. Maybe they weren’t fully reassured about their recovery."

            doctor_sycamore "It seems like they had some concerns that weren’t completely addressed, but they’re still grateful for the care they received."

            you "I see… I’ll make sure to be more mindful of that next time."

            doctor_sycamore "That’s the right attitude. You did well in terms of treatment, but remember, bedside manner is just as important as medical skill."

            doctor_sycamore "Every patient deserves care that not only heals them physically but also puts them at ease mentally."

            you "Understood, doc. I’ll make sure to improve my communication and reassurance next time."

            doctor_sycamore "That’s all I ask. Keep learning from each experience, and you’ll become an even better doctor."

            "You nod, taking his words to heart as you leave the office, determined to do better in the future."
                
            label bad_ending:
                scene office at clinic_default
            "You proceed to Doctor Sycamore's office to report and verify the case of the patient."
            "You knock on Doctor Sycamore's office door."

            doctor_sycamore "Come in!"

            "You step inside hesitantly, sensing that this conversation might not be a pleasant one."

            doctor_sycamore "Welcome back, doc. I hate to say it, but we’ve got some concerns about your handling of the patient’s case."

            you "What happened, doc?"

            doctor_sycamore "Well… let's just say your approach in talking to the patient didn’t go too well."

            you "Did I say something wrong?"

            doctor_sycamore "It’s not just what you said—it’s how you said it. The patient left feeling confused and uncertain about their recovery."

            doctor_sycamore "They didn’t feel reassured, and they were worried about what comes next. That’s not what we want."

            you "I see… I should’ve been more careful with my explanations."

            doctor_sycamore "Exactly. Patients are already stressed when they come in. The way we communicate can either put them at ease or make them feel worse."

            doctor_sycamore "I know you meant well, but you need to work on your bedside manner. Medical skill is important, but so is how you interact with patients."

            you "I understand, doc. I’ll work on improving that."

            doctor_sycamore "Good. Because next time, I expect you to do better."

            "Feeling disappointed in yourself but determined to improve, you leave the office with a new understanding of how important patient communication is."

            return