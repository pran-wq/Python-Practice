from fpdf import FPDF
import textwrap

class PDF(FPDF):
    def header(self):
        # Logo or Header Text
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, 'Innovation and Design Thinking (1BIDTL108) - Observation Phase Report', 0, 1, 'R')
        self.ln(5)

    def footer(self):
        # Position at 1.5 cm from bottom
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, 'Page ' + str(self.page_no()) + '/{nb}', 0, 0, 'C')

    def chapter_title(self, title):
        self.set_font('Arial', 'B', 14)
        self.cell(0, 10, title, 0, 1, 'L')
        self.ln(4)

    def chapter_body(self, body):
        self.set_font('Times', '', 12)
        # Output justified text
        self.multi_cell(0, 8, body)
        self.ln()

# Create instance of FPDF class
pdf = PDF()
pdf.alias_nb_pages()

# --- CONTENT DEFINITIONS ---

# Title Page Content
title_page_text = """
INNOVATION AND DESIGN THINKING (1BIDTL108)

PART B: OBSERVATION PHASE REPORT


Project Title:
Decentralized P2P Mesh Network for Offline Messaging and File Sharing


Submitted by:
1. SUJITH C (25UG1BYCS0221-T)
2. NISHCHAL KUMAR KARN (25UG1BYCS0396-T)
3. PRANAV RAJ (25UG1BYCS0783-T)
4. VINAY KUMAR (25UG1BYCS0610-T)


Course Coordinator:
Prof. Mahalakshmi Gopinath

Department:
Computer Science & Engineering

Date:
November 24, 2025
"""

# Section Content (Mapped to the report structure)
sections = [
    ("1. Objectives of Observation Phase", """The primary objective of the Observation Phase is to move beyond theoretical assumptions and witness the actual struggles users face when centralized communication infrastructure fails. By observing users in real-world or simulated "offline" scenarios, we aim to:

1. Validate the Problem Statement: Confirm that internet dependency causes significant anxiety, helplessness, and operational failure during network outages.
2. Analyze User Behavior in "Dead Zones": Observe the physical and cognitive actions users take when they see "No Signal" or "Message Failed," such as frantically searching for Wi-Fi or physically moving to find a signal.
3. Understand the Environment: Document the specific environments where P2P mesh networking is most needed, such as crowded events, remote rural areas, and disaster-prone zones.
4. Identify Latent Needs: Uncover needs that users might not articulate in interviews, such as the need for "confirmation" that a message has been queued even if it hasn't been sent yet.
5. Assess Technical Constraints: Observe how battery drain and OS restrictions (like background app killing) currently affect user behavior with existing apps."""),

    ("Bt2: TIPS FOR OBSERVING", """To ensure high-quality data collection, the observation strategy was planned as follows:

a) Who should be observed?
We identified three distinct user groups based on our "Search Field Determination":
1. The "Disconnect" Victim: General users (students/families) experiencing network congestion at large events (e.g., college fests, concerts) where standard cellular networks fail due to load.
2. The Remote Dweller: Individuals in rural areas where internet penetration is low, data costs are high, and mobile infrastructure is sparse.
3. The Privacy Conscious: Users who actively avoid centralized servers (Meta/Google) due to surveillance concerns and seek end-to-end encrypted alternatives.

b) Who should carry out the observation?
The observation is conducted by the development team (Sujith, Nishchal, Pranav, Vinay) to ensure that technical insights (regarding Bluetooth/Wi-Fi limitations) are captured alongside behavioral data.

c) Which behaviour should be observed?
1. The "Signal Hunt": Users raising phones, walking to windows, or toggling Airplane mode on/off when connection is lost.
2. Error Handling: Reactions to "Message Not Sent" notifications-frustration, repeated tapping of the "retry" button, or switching apps.
3. Battery Anxiety: How often users check their battery percentage when searching for a signal, as searching drains power.
4. Analog Fallback: When digital comms fail, do users resort to shouting, walking to find people, or giving up?

d) How are the observations recorded?
- AEIOU Matrix: A structured grid to log details.
- Video/Photo Documentation: Capturing the "No Service" screens and user facial expressions (with consent).
- Field Notes: Real-time logging of user quotes and actions."""),

    ("Bt3: DIFFERENT DIMENSIONS OF DESCRIPTIVE OBSERVATION (AEIOU) - Scenario 1", """Observation Context 1: The High-Density Event (College Fest/Concert)
Rationale: Simulates network congestion where centralized towers fail.

a) SPACE
- Physical: An open-air stadium or auditorium packed with thousands of people.
- Atmosphere: Noisy, chaotic, high energy.
- Network Status: Full signal bars might be visible, but data throughput is zero due to bandwidth congestion. "Fake signal" phenomenon.

b) ACTORS
- Students: Trying to find friends in the crowd.
- Organizers: Trying to coordinate logistics (security, stage management) without walkie-talkies.
- Vendors: Trying to process digital payments (which fail without internet).

c) GOALS
- Immediate: "I need to tell my friend I am at the North Gate."
- Secondary: Share a photo/video of the event in real-time.
- Outcome: To coordinate a meetup point amidst the crowd.

d) FEELINGS
- Frustration: Visibly annoyed when messages stick on "Sending..."
- Anxiety: "I can't find my group, and I don't know where to go."
- Resignation: Putting the phone away and realizing digital communication is useless."""),

    ("Bt3: DIFFERENT DIMENSIONS OF DESCRIPTIVE OBSERVATION (AEIOU) - Scenario 2", """Observation Context 2: The Remote/Rural Trek
Rationale: Simulates a complete lack of infrastructure.

a) SPACE
- Physical: Dense forest trail or a remote village with hills blocking cell towers.
- Atmosphere: Quiet, isolated, physically demanding terrain.
- Network Status: "No Service" / "Emergency Calls Only."

b) ACTORS
- Trekkers/Travelers: Group of 4-5 people.
- Local Villagers: Residents who have no ISP coverage.

c) GOALS
- Safety: "I need to check if the trailing group is safe."
- Navigation: Sharing a location pin or map data.
- Emergency: In case of injury, contacting the base camp.

d) FEELINGS
- Fear/Vulnerability: "If something happens, we can't call for help."
- Isolation: The psychological weight of being "cut off" from the world."""),

    ("Bt3: DIFFERENT DIMENSIONS OF DESCRIPTIVE OBSERVATION (AEIOU) - Scenario 3", """Observation Context 3: The Simulated "Blackout" (Privacy/Censorship)
Rationale: Simulates government-imposed shutdowns or privacy concerns.

a) SPACE
- Physical: Urban environment, perhaps a protest site or a region under internet curfew.
- Digital: Centralized apps (WhatsApp/Telegram) are blocked by firewalls.

b) ACTORS
- Activists/Journalists: Need to share information without being tracked.
- General Citizens: Trying to contact family during a shutdown.

c) GOALS
- Evasion: Communicate without metadata logging by ISPs or central servers.
- Resilience: Keep information flowing despite the internet ban.

d) FEELINGS
- Paranoia: "Is this channel secure? Who is listening?"
- Distrust: Skepticism towards standard apps like SMS or unencrypted calls.
- Empowerment: The relief of finding a tool that works "under the radar." """),

    ("Bt4: DIFFERENT FACTORS OF CUSTOMER EXPERIENCE", """Analyzing how users interact with current connectivity limitations helps us design a better P2P solution.

a) Physical Factors
- The "Signal Dance": We observed users holding phones high in the air, walking in circles, or leaning out of windows. This is a physical manifestation of the invisible problem of connectivity.
- Battery Heat: Constant searching for a cellular signal causes the phone to heat up physically. Users become annoyed and often turn off their phones to save power, further isolating them.
- Touch Interactions: Repeatedly pulling down the "Notification Shade" to toggle Wi-Fi or Mobile Data, hoping a reset will fix the connection.

b) Cognitive Factors
- Confusion: Users often don't understand why they can't send a message. "I have full bars, why isn't WhatsApp working?" (Congestion vs. Coverage).
- Mental Load: Users have to remember "Who is near me?" vs "Who is far away?" In a P2P mesh, this cognitive model changes. They need to understand that the people are the network.
- Trust: Users struggle to trust an app that claims to work "without internet." It contradicts their mental model of how smartphones work."""),

    ("Bt4: DIFFERENT FACTORS OF CUSTOMER EXPERIENCE (Continued)", """c) Social Factors
- Proximity-Based Interaction: Without internet, social interaction shrinks to physical proximity. People stop messaging and start looking for faces.
- Crowd Coordination: In festivals, we observed "chains" of people passing verbal messages. Our P2P app aims to digitize this "human chain" via multi-hop routing.
- The "Hotspot" Beggar: A common social interaction is asking, "Can you turn on your hotspot?" This creates a social debt. A mesh network democratizes this by making everyone a node automatically.

d) Emotional Factors
- FOMO (Fear Of Missing Out): High anxiety when social feeds don't refresh.
- Panic: In emergency drills, the inability to contact family induces immediate panic.
- Relief: The moment a message finally delivers (one tick becomes two ticks), there is a visible sigh of relief. Our goal is to provide that "Delivered" state even when offline."""),

    ("B16: EMPATHY MAP (User 1: The Disaster Survivor)", """User Profile: Someone in a flood-prone area or earthquake zone.

A) What does the person think and feel?
- Thoughts: "Are the rescue teams coming?", "Is the bridge ahead flooded?", "I have 10% battery left, I need to make it count."
- Feelings: Intense fear, helplessness, isolation. A desperate need for information, not entertainment.

B) What does the person say and do?
- Says: "No signal! Does anyone have a radio?", "Don't use the phone for videos, save battery."
- Do: Moves to higher ground seeking signal. Tries to send SMS repeatedly.

C) What does the person hear?
- Hear: Sirens, rain, wind. Rumors spreading among neighbors because official news channels (internet/TV) are down.
- Influence: Neighbors saying, "The towers are down for 48 hours."

D) What does the person see?
- See: Destruction of infrastructure (fallen poles). Phones showing "Emergency Calls Only."
- See: Rescue boats passing by but unable to communicate with them directly.

E) Pain (Frustrations)
- Complete inability to coordinate rescue.
- Not knowing if loved ones are safe.
- Phone battery dying while searching for a signal.

F) Gain (Goals)
- A simple "I am safe" message delivered to family.
- Receiving a broadcast alert about food/water locations."""),

    ("B16: EMPATHY MAP (User 2: The Student Activist)", """User Profile: A student organizing a protest or event in a censored region.

A) What does the person think and feel?
- Thoughts: "They might shut down the internet to stop us from organizing.", "I don't want the government reading my chats."
- Feelings: Defiant but paranoid. Values privacy above convenience.

B) What does the person say and do?
- Says: "Switch to Signal," "Turn off your location history," "Meet at the square."
- Do: Uses VPNs (which might be blocked). Looks for alternative offline communication tools like Bridgefy or our proposed app.

C) What does the person hear?
- Hear: Reports of other activists being arrested based on WhatsApp metadata.
- Influence: Online forums discussing "Cyber Hygiene" and "Mesh Networking."

D) What does the person see?
- See: Internet speed throttling. Websites failing to load.
- See: Police presence monitoring the crowd.

E) Pain (Frustrations)
- Centralized servers are single points of failure and surveillance.
- Metadata logging (who spoke to whom) acts as evidence against them.

F) Gain (Goals)
- Anonymous, ephemeral communication.
- A network that cannot be "switched off" by a central authority."""),

    ("B16: EMPATHY MAP (User 3: The Rural Villager)", """User Profile: A resident of a remote village with poor infrastructure.

A) What does the person think and feel?
- Thoughts: "Data is too expensive to use just for chatting.", "The tower only works on the hill, not in my house."
- Feelings: Frustration with the "Digital Divide." Feels left behind by technology.

B) What does the person say and do?
- Says: "I'll wait until I go to the town to download the file.", "Turn off data, it costs money."
- Do: Uses Bluetooth (ShareIt) for file transfer but wishes they could text comfortably.

C) What does the person hear?
- Hear: City people talking about 5G, while they barely have 2G.
- Influence: Community leaders using loudspeakers for announcements because group chats don't work reliably.

D) What does the person see?
- See: "E" (Edge) network symbol or "No Service."
- See: High bills for mobile recharge.

E) Pain (Frustrations)
- High cost of staying connected.
- Unreliable connection that drops mid-conversation.

F) Gain (Goals)
- Free, local communication with neighbors.
- Sharing photos/videos without using paid data."""),

    ("Bt6: COGNITIVE WALKTHROUGH", """We analyzed the cognitive process of a user attempting to use our P2P Offline Messenger for the first time during an outage.

User Task: Send a message to a friend 200 meters away (out of direct range, requiring a "hop") without Internet.

a) What would the user perceive and think?
- Perception: The user opens the app. They expect it to look like WhatsApp.
- Thought: "My internet is off. Will this actually work? How does it find my friend?"
- Challenge: The concept of "Discovery" takes time (5-10 seconds) unlike instant server connections. The user might think the app is broken.

b) Complexity Analysis
- Discovery Phase: The user must grant permissions for "Nearby Devices," "Bluetooth," and "Location." This is a high barrier. If they deny one, the mesh fails.
- Connection Phase: The app automatically negotiates keys (Curve25519). The user shouldn't see this, but they need visual feedback that "Secure Connection Established."

c) Identifying Barriers
- Barrier 1: iOS Restrictions. Apple kills background processes. The user might need to keep the screen on for the mesh to work, which is counter-intuitive.
- Barrier 2: Empty List. If no one else around has the app, the list is empty. This "Cold Start" problem is the biggest cognitive hurdle.

d) Difficulty for the User
- Understanding the "Hop": The user sends a message to person C. They need to understand it might go through Person B.
- Latency: Mesh networks are slower. The user needs patience, which modern users lack."""),

    ("Bt6: COGNITIVE WALKTHROUGH (Continued)", """e) Reduction of Complexity (Proposed Solutions)
1. Automated Discovery: Instead of a "Scan" button, the app scans in the background using BLE (Bluetooth Low Energy) to minimize user effort.
2. Visual Topology: Show a map or graph of connected nodes (e.g., "You are connected to 3 peers") to visualize the invisible network.
3. Store-and-Forward Feedback: If a path isn't found immediately, show "Queued for delivery when peer appears" instead of "Failed".

j) User Profile for Walkthrough
- Name: Rahul (Undergraduate Student).
- Tech Literacy: High.
- Context: Campus Wi-Fi is down during an exam. Needs to ask a friend for notes.
- Goal: Transfer a PDF file using the Mesh.

o) Will the user achieve the goal?
- Yes, provided that:
  1. The friend also has the app open.
  2. They are within the 100m Bluetooth range or have intermediate peers to bridge the gap."""),

    ("Bt7: HEURISTIC EVALUATION", """We evaluated the proposed P2P App design against Nielsen's 10 Usability Heuristics, specifically focusing on the challenges of offline networking.

a) Visibility of System Status
- Issue: In standard apps, "Online" means connected to a server. In a Mesh, "Online" is relative.
- Solution: The app must clearly display "Direct Connection" vs. "Mesh Connection" and show signal strength relative to peers, not cell towers.
- Metric: Display "Peers Nearby: 5" in the header at all times.

b) Match Between System and Real World
- Issue: Technical terms like "TTL" (Time To Live), "Hops," and "Nodes" are confusing.
- Solution: Use natural language. Instead of "3 Hops," say "Relayed via 2 people." Instead of "Node," say "User" or "Peer".

c) User Control and Freedom
- Issue: Users might unknowingly relay messages for others, draining their battery.
- Solution: Provide a toggle: "Relay Mode: ON/OFF." Allow users to choose if they want to participate in the routing or just be a passive endpoint.

d) Consistency and Standards
- Standard: Use the familiar "Double Check Mark" (Sent/Delivered) UI pattern found in WhatsApp/Signal.
- Consistency: The chat interface should look identical to standard SMS apps to reduce the learning curve."""),

    ("Bt7: HEURISTIC EVALUATION (Continued)", """e) Error Prevention
- Risk: Users might turn off Bluetooth to save battery, breaking the mesh.
- Prevention: A persistent notification asking "Keep Bluetooth ON to stay connected to the mesh."
- Security Error: Users might try to send sensitive data over an unverified hop.
- Prevention: Auto-verify keys and show a "Padlock" icon for End-to-End Encryption.

f) Recognition Rather Than Recall
- Issue: Users can't remember IP addresses or complex Hashes.
- Solution: Use QR codes for initial peer exchange to "Introduce" devices to each other securely.

g) Flexibility and Efficiency of Use
- Feature: Hybrid switching.
- Detail: The app should automatically switch between Bluetooth LE (for text) and Wi-Fi Direct (for heavy files) without user intervention.

h) Aesthetic and Minimalist Design
- Constraint: Mesh apps process heavy data in the background. The UI must be lightweight to keep the app responsive.
- Design: Dark Mode default to save battery on OLED screens (crucial for disaster scenarios)."""),

    ("Bt8: CRITICAL-INCIDENT TECHNIQUE", """We interviewed 5 potential users about specific past incidents where communication failure led to significant distress.

Incident 1: The Trekking Accident
- User: An avid hiker.
- Context: Coorg, Karnataka (Deep forest).
- Incident: One trekker twisted an ankle. The group split up to find help.
- The Failure: The group remaining behind had no way to know if the forward group had reached the road. They waited 6 hours in panic.
- Relevance: A P2P mesh (via intermediate trekkers) could have allowed the forward group to relay a "Help found" message back up the trail.

Incident 2: The Festival Separation
- User: A college student.
- Context: Sunburn Festival.
- The Failure: User lost their friends. WhatsApp messages were stuck on "Clock" icon (Sending) for 3 hours due to network congestion.
- Consequence: The user spent the entire concert alone and anxious near the exit gate.
- Relevance: Bluetooth works perfectly in high-density crowds. This was a missed opportunity for P2P networking."""),

    ("Bt8: CRITICAL-INCIDENT ANALYSIS", """Incident 3: The Flood Response (Chennai Floods)
- User: A volunteer coordinator.
- Context: Urban flood zone, power cut for 3 days.
- The Failure: Cell towers ran out of diesel backup. Volunteers in boats could not communicate with the supply trucks 1km away.
- Consequence: Food packets were delivered to the wrong area while another area went hungry.
- Relevance: A localized, infrastructure-independent mesh could have coordinated the logistics over that 1km distance effectively.

Analysis of Incidents:
1. Common Thread: In all cases, the devices (smartphones) were functional and charged, but the infrastructure (towers) failed.
2. Distance: The communication gap was often short (500m - 2km)-perfect for a multi-hop mesh network.
3. Psychological Impact: The lack of information caused more distress than the physical situation itself."""),

    ("Technical Observations & Constraints", """Beyond user behavior, we observed the technical behavior of the hardware involved in the project.

1. Battery Consumption
- Observation: Continuous BLE scanning drains approximately 8-12% battery per hour on standard Android devices if not optimized.
- Constraint: Users in disaster zones prioritize battery life over everything.
- Implication: We must implement "Adaptive Duty Cycles" (scan for 10 seconds, sleep for 50 seconds) to reduce drain.

2. OS Restrictions (The "Android Doze" Problem)
- Observation: Android OS puts background apps to sleep to save battery.
- Constraint: If the P2P app is killed, the mesh node breaks.
- Implication: We must use a foreground service (persistent notification) to keep the mesh alive.

3. Bandwidth Limitations
- Observation: Bluetooth Low Energy (BLE) has very low bandwidth (~2 Mbps theoretical, much lower in practice).
- Constraint: Sending large photos takes too long and congests the mesh.
- Implication: We must strictly compress images or switch to Wi-Fi Direct for file transfers, keeping BLE for text only."""),

    ("Conclusion of Observation Phase", """The Observation Phase has provided critical insights that validate the need for a Decentralized P2P Mesh Network.

Key Findings:
1. The problem is universal: Whether it is a student at a concert, a villager in a remote area, or a victim of a disaster, communication breakdown leads to anxiety, confusion, and operational failure.
2. The infrastructure is the bottleneck: In most scenarios, smartphones remain functional, but towers, backhaul, or government-imposed restrictions break connectivity.
3. The distances are local: Most urgent communication needs occur within a short physical radius (friends, family, volunteers) where multi-hop Bluetooth/Wi-Fi links are feasible.
4. Psychological relief matters as much as bandwidth: Even a small "I'm safe" or "On my way" message dramatically reduces stress.

These observations strongly justify continuing to the Ideation and Prototyping phases, focusing on a resilient, user-friendly, offline-first mesh networking solution that turns nearby users into a cooperative communication infrastructure.""")
]

# Now actually build the PDF
pdf.add_page()
pdf.set_font('Arial', 'B', 16)
pdf.multi_cell(0, 10, title_page_text, align='C')
pdf.add_page()

for title, body in sections:
    pdf.chapter_title(title)
    pdf.chapter_body(body)

# Output file
pdf.output("Observation_Phase_Report.pdf")
print("PDF GENERATED SUCCESSFULLY 🎉")
