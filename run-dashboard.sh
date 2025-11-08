#!/bin/bash

echo "🚀 Market Risk Dashboard (dashboard.py) 실행 중..."
echo "📍 포트: 8501"
echo "🌐 접속 주소: http://localhost:8501"
echo ""

# 기존 컨테이너 정리
echo "🧹 기존 컨테이너 정리 중..."
docker-compose -f docker-compose.dashboard.yml down

# 새로 빌드하고 실행
echo "🔨 Docker 이미지 빌드 중..."
docker-compose -f docker-compose.dashboard.yml up -d --build

echo ""
echo "✅ 대시보드가 성공적으로 실행되었습니다!"
echo "🌐 브라우저에서 http://localhost:8501 으로 접속하세요"
echo ""
echo "📋 유용한 명령어:"
echo "  - 로그 확인: docker-compose -f docker-compose.dashboard.yml logs dashboard"
echo "  - 중지: docker-compose -f docker-compose.dashboard.yml down"
echo "  - 재시작: docker-compose -f docker-compose.dashboard.yml up -d" 