<<<<<<< HEAD
echo "start"
pip install -r requirements.txt
python3.9 manage.py collectstatic --noinput --clear
echo "end:
=======
echo "BUILD START"
pip install -r requirements.txt
python3.9 manage.py collectstatic  --noinput --clear
echo "END BUILD"
>>>>>>> ffe58d96037b2685c026033b814afdd9f61a2a5a
