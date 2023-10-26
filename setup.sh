echo -e "\e[1;32m---Virtual-Enviromnent-Python Setup---\e[0m"
echo ""
echo "1. remove a venv if it already exists"

rm -rf venv
echo ""
echo "2.check python version (requires python 3.10.X)"

pyv="$(python -V 2>&1)"
SUB='3.10'
if [[ "$pyv" == *"$SUB"* ]]; then
  echo "python version $pyv is valid."
else
    echo "WRONG VERSION OF PYTHON. You'll need to install python version 3.10.X"
    echo "exiting script..."
    exit
fi
echo ""

echo "3. setup virtual environment"
rm -rf venv
python -m venv venv
source venv/bin/activate
pip install --upgrade pip > /dev/null
echo ""
echo "4. installing packages"
pip install -r requirements.txt > /dev/null
echo ""

echo "package installation complete"
echo "to deactivate venv, use command $ deactivate"
echo ""
echo -e "\e[1;32m---virtual env setup complete.---\e[0m"
