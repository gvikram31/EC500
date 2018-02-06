export GOOGLE_APPLICATION_CREDENTIALS="/home/mjhuria/Desktop/google_key.json"
cd pictures/
find . -iname '*.jpg' -delete
cd ../src/
python run.py $1
echo $1
cd ../pictures/
ffmpeg -y -loop 1 -i %d.jpg -c:a libfdk_aac -ar 44100 -ac 2 -vf "scale='if(gt(a,16/9),1280,-1)':'if(gt(a,16/9),-1,720)', pad=1280:720:(ow-iw)/2:(oh-ih)/2" -c:v libx264 -b:v 10M -pix_fmt yuv420p -r 30 -shortest -avoid_negative_ts make_zero -fflags +genpts -t 1 output.mp4

