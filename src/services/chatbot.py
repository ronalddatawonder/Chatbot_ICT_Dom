"""
ICT FAQ Chatbot using Streamlit
Handles simple exact-match FAQ responses for ICT-related questions
"""
import streamlit as st

# Dictionary met voorgedefinieerde vragen en antwoorden
ict_faqs = {
    # --- Wachtwoord Gerelateerd ---
    "ik ben mijn wachtwoord vergeten": "Om je wachtwoord te resetten, ga naar [link naar self-service portal] en klik op 'Wachtwoord vergeten'. Volg de instructies.",
    "hoe reset ik mijn wachtwoord?": "Om je wachtwoord te resetten, ga naar [link naar self-service portal] en klik op 'Wachtwoord vergeten'. Volg de instructies.",
    "wachtwoord resetten": "Om je wachtwoord te resetten, ga naar [link naar self-service portal] en klik op 'Wachtwoord vergeten'. Volg de instructies.",
    "ik weet mijn wachtwoord niet meer": "Geen probleem. Om je wachtwoord te resetten, ga naar [link naar self-service portal] en klik op 'Wachtwoord vergeten'. Volg de instructies.",

    # --- Printer Gerelateerd ---
    "mijn printer werkt niet": "1. Controleer of de printer aanstaat en verbonden is (USB/Netwerk).\n2. Controleer papier en toner/inkt.\n3. Start printer en computer opnieuw op.\n4. Werkt het nog steeds niet? Probeer de printer troubleshooter: [link] of neem contact op.",
    "hoe installeer ik een printer?": "Volg de handleiding op [link naar printer installatie handleiding] om een netwerkprinter toe te voegen.",
    "printer offline": "Controleer de netwerkverbinding van de printer. Start de printer opnieuw op. Controleer of hij als standaardprinter is ingesteld. Zie ook: [link naar troubleshooting]",

    # --- Software & Applicaties ---
    "hoe installeer ik software?": "Goedgekeurde software kan geïnstalleerd worden via het 'Software Center' op je bureaublad. Zoek de software en klik op 'Installeren'.",
    "software center werkt niet": "Probeer je computer opnieuw op te starten. Als het Software Center daarna nog steeds niet werkt, neem contact op met de Servicedesk.",
    "teams start niet op": "1. Sluit Teams volledig af (via Taakbeheer indien nodig).\n2. Start Teams opnieuw.\n3. Start je computer opnieuw op.\n4. Als het probleem blijft, probeer Teams cache te legen: [link naar handleiding]",
    "outlook problemen": "Voor algemene Outlook problemen (niet opstarten, vastlopen), probeer eerst Office te herstellen via 'Apps & Functies' -> Microsoft 365 Apps -> Wijzigen -> Online herstellen.",

    # --- Netwerk & Verbinding ---
    "vpn verbinding maken lukt niet": "1. Controleer je internetverbinding.\n2. Controleer of je de juiste VPN-server en inloggegevens gebruikt.\n3. Start de VPN-client (bv. FortiClient, Cisco AnyConnect) opnieuw.\n4. Start je computer opnieuw op.\nZie handleiding: [link]",
    "geen internet": "1. Controleer of je netwerkkabel goed is aangesloten (indien van toepassing).\n2. Controleer of Wi-Fi is ingeschakeld en je met het juiste netwerk verbonden bent.\n3. Start je computer en de modem/router (indien thuis) opnieuw op.\n4. Als collega's ook problemen hebben, meld het bij de Servicedesk.",

    # --- Overig ---
    "hoe vraag ik een nieuwe laptop aan?": "Het aanvragen van nieuwe hardware verloopt via [link naar aanvraagportaal of procedure beschrijving].",
    "scherm blijft zwart": "1. Controleer of de monitor aanstaat en de kabels (stroom, video) goed zijn aangesloten.\n2. Probeer de monitor op een andere computer of een andere monitor op jouw computer.\n3. Druk op Ctrl+Alt+Del om te zien of er reactie is.\nNeem anders contact op."
}

def initialize_session_state():
    """Initialize session state variables if they don't exist"""
    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = []

def get_bot_response(user_input: str) -> str:
    """
    Get bot response based on user input
    Uses exact (case-insensitive) matching
    """
    # Convert user input to lowercase for case-insensitive matching
    user_input = user_input.lower().strip()
    
    # Check for exact match in FAQ dictionary
    if user_input in ict_faqs:
        return ict_faqs[user_input]
    
    # No match found
    return "Sorry, ik kon geen direct antwoord vinden op die precieze vraag. Probeer het anders te formuleren of neem contact op met de ICT Servicedesk via [telefoonnummer/email/portaal]."

def main():
    # Initialize session state
    initialize_session_state()
    
    # Set page title and header
    st.title("ICT Helpdesk Assistent")
    st.markdown("Stel je vraag over ICT-gerelateerde problemen. Typ je vraag *exact* zoals deze in de lijst staat.")
    
    # Chat input
    user_input = st.chat_input("Typ je vraag hier...")
    
    # Handle user input
    if user_input:
        # Add user message to chat history
        st.session_state.chat_history.append({"role": "user", "content": user_input})
        
        # Get bot response
        bot_response = get_bot_response(user_input)
        
        # Add bot response to chat history
        st.session_state.chat_history.append({"role": "assistant", "content": bot_response})
    
    # Display chat history
    for message in st.session_state.chat_history:
        with st.chat_message(message["role"]):
            st.write(message["content"])

if __name__ == "__main__":
    main()