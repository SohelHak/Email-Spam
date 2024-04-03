echo "Giving executable permission to spam.py......."
chmod +x dependency/spam.py

echo "Installing Python3........"
apt install python3

clear
echo "Installing Requirement packages........"
pip3 install -r dependency/requirements/requirement.txt
clear

echo "Moving spam.py......."
mv dependency/spam.py /usr/bin/e-spam

cd ..
rm -rf Email-Spam
cd 
clear

echo """Type 'e-spam', to run tool



Note: This email spam tool has been developed for educational purposes only. It is intended to demonstrate concepts related to email automation and should be used responsibly and ethically. Misuse of this tool for sending unsolicited or unauthorized emails is strictly prohibited and may violate laws and regulations related to email spamming and privacy. The developer assumes no liability for any misuse of this tool. Users are responsible for ensuring compliance with all applicable laws and regulations when using this tool. Use it responsibly and always respect the privacy and consent of others.
"""
cd $HOME
