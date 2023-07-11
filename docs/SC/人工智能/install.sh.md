```shell
#!/bin/bash

restart_interval=6
if [ $1 ];then
  restart_interval=$1
fi

project_path=$(pwd)
project_name="${project_path##*/}"


echo ""
echo ""
echo "START CLEAR"
docker stop $(docker ps -a | grep boxeye-service | awk '{print $1}')
docker container rm $(docker ps -a | grep Exited | awk '{print $1}')
ps -aux | grep 'sync_config.py' | cut -c 9-15 | xargs kill -9
rm -rf /workspace
rm -rf ossutil*
systemctl stop sync_daemon.service


echo ""
echo ""
echo "START INSTALL"
mkdir /workspace
mkdir /workspace/assets
mkdir /workspace/assets/config
mkdir /workspace/assets/facedb
mkdir /workspace/assets/models
mkdir /workspace/assets/output
mkdir /workspace/assets/log
mkdir /workspace/code
chmod -R 777 /workspace
cd ../
cp -r $project_name /workspace/code/


#wget https://gosspublic.alicdn.com/ossutil/1.7.13/ossutil64
#chmod 755 ossutil64
#./ossutil64 config -e $endpoint -i $id -k $key
#./ossutil64 cp -r -f oss://aibox-assets/assets/models /workspace/assets/
#./ossutil64 cp -r -f oss://aibox-assets/assets/config /workspace/assets/


echo ""
echo ""
echo "DOWNLOAD ASSETS"
cd /workspace/assets/models
wget https://aieye-1303022215.cos.ap-shanghai.myqcloud.com/aibox-assets/assets/models/bytetrack_x_fp16.trt
wget https://aieye-1303022215.cos.ap-shanghai.myqcloud.com/aibox-assets/assets/models/face_detection_fp16.trt
wget https://aieye-1303022215.cos.ap-shanghai.myqcloud.com/aibox-assets/assets/models/face_recognition_fp16.trt
cd ../config
wget https://aieye-1303022215.cos.ap-shanghai.myqcloud.com/aibox-assets/assets/config/config.yml


echo ""
echo ""
echo "START RUN MAIN PROGRAM"
cd /workspace/code/$project_name/aibox
sh deploy.sh


echo ""
echo ""
echo "START REGISTER DAEMON PROCESS"
cd ../
service_exec_start="ExecStart=\/workspace\/code\/"$project_name"\/daemon_start.sh"
service_exec_stop="ExecStop=\/workspace\/code\/"$project_name"\/daemon_stop.sh"
sed -i 's/ExecStart=/'$service_exec_start'/' sync_daemon.service
sed -i 's/ExecStop=/'$service_exec_stop'/' sync_daemon.service
chmod +x daemon_start.sh
chmod +x daemon_stop.sh
cp sync_daemon.service /etc/systemd/system/
systemctl daemon-reload


echo ""
echo ""
echo "START RUN DAEMON PROGRAM"
python3 aibox/print_mac_id.py
systemctl start sync_daemon.service
systemctl enable sync_daemon.service

```