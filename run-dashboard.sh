#!/bin/bash

echo "🚀 Market Risk Dashboard (main.py) 실행 중..."
echo "📍 포트: 8501"
echo "🌐 접속 주소: http://localhost:8501"
echo ""

# 기존 Streamlit 프로세스 종료
echo "🧹 기존 프로세스 정리 중..."
pkill -f "streamlit run main.py" 2>/dev/null
sleep 2

# 가상환경 활성화 및 Streamlit 실행
echo "🔨 Streamlit 대시보드 시작 중..."
cd "$(dirname "$0")"

# 가상환경이 있으면 활성화
if [ -d "venv" ]; then
    source venv/bin/activate
    streamlit run main.py --server.port=8501 --server.address=localhost &
else
    # 가상환경이 없으면 시스템 Python 사용
    streamlit run main.py --server.port=8501 --server.address=localhost &
fi

sleep 3

echo ""
echo "✅ 대시보드가 성공적으로 실행되었습니다!"
echo "🌐 브라우저에서 http://localhost:8501 으로 접속하세요"
echo ""
echo "📋 유용한 명령어:"
echo "  - 중지: pkill -f 'streamlit run main.py'"
echo "  - 로그 확인: ps aux | grep streamlit" 