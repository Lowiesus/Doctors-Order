# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")
define dc = Character("Sycamore")


# The game starts here.

label start:


    # Scene: Loading Screen
    label hints:
        scene hospital_lobby
        "Butot balat lumilipad"

    scene hospital_day
    with fade

    "You are a new resident doctor in St. Angels Hospital."

    # Scene 1: Patient’s Arrival
    label patient_arrival:
        scene hospital_lobby
        "A teenager arrives at the hospital with a knee injury from a soccer game."
        "The patient looks nervous as they sit down in the waiting area."

        menu:
            "How do you approach the patient?"
            "Hi, my name is Doctor Jest. You’re in good hands and we’ll do our best to take care of you. Now what happened with your knee? Do you have previous medical treatments that we should know about?":
                jump diagnostics
            "What happened with your knee?":
                "The patient seems a little nervous. Maybe a friendlier tone would help."
                jump diagnostics
            "Ermmm, your knee looks bad. What happened?":
                "The patient looks uncomfortable and more anxious."
                jump diagnostics

    # Scene 2: Diagnostic Process - Performing Tests
    label diagnostics:
        scene exam_room
        "You move the patient to the examination room and observe the knee."

        menu:
            "What do you say while performing the diagnostic?"
            "I’ll be checking your knee, let me know if anything hurts okay?":
                jump diagnosis_result
            "We need an X-ray to see inside the knee and check for tearing or fractures.":
                "The patient nods but still looks worried."
                jump diagnosis_result
            "We will proceed to do some tests, you’ll find out soon enough.":
                "The patient frowns and looks confused."
                jump diagnosis_result

    # Scene 3: Diagnosis Confirmation
    label diagnosis_result:
        scene xray_review
        "The X-ray shows a clear kneecap fracture. The patient waits nervously."

        menu:
            "How do you deliver the news?"
            "Your knee has a fracture - which is treatable, and don’t worry! We’ll walk you through every step of the operation.":
                jump surgery_prep
            "You’ll need surgery to fix your knee. It's common and you’ll surely recover.":
                "The patient tries to stay calm."
                jump surgery_prep
            "Dang, your knee is broken, we’ll have to operate on it.":
                "The patient looks alarmed."
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
        "Thank you for playing PixelCure!"

    return
