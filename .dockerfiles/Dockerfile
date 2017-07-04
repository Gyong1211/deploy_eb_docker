FROM        eb_ubuntu
MAINTAINER gyong1211@gmail.com

# 현재 경로의 모든 파일(프로젝트 파일)을 컨테이너의 /srv/deploy_eb_docker 폴더에 복사
COPY        . /srv/deploy_eb_docker
# 쉘에서 입력하는 cd /srv/deploy_eb_docker와 같은 명령어
WORKDIR     /srv/deploy_eb_docker
# requirements 설치
RUN         /root/.pyenv/versions/deploy_eb_docker/bin/pip install -r .requirements/debug.txt

# supervisor file 복사
COPY        .config/supervisor/uwsgi.conf /etc/supervisor/conf.d/
COPY        .config/supervisor/nginx.conf /etc/supervisor/conf.d/

# nginx파일 복사
COPY        .config/nginx/nginx.conf /etc/nginx/nginx.conf
COPY        .config/nginx/nginx-app.conf /etc/nginx/sites-available/nginx-app.conf
RUN         rm -rf /etc/nginx/sites-enabled/default
RUN         ln -sf /etc/nginx/sites-available/nginx-app.conf /etc/nginx/sites-enabled/nginx-app.conf

CMD         supervisord -n

EXPOSE 80 8000