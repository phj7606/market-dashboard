# Market Risk Dashboard - 빠른 시작 가이드

## 🚀 앱 실행 방법

### 로컬에서 실행
```bash
cd "/Users/HuiJune Park/I AI/Cursor/Project/Market Signal/Market Risk"
streamlit run main.py
```
브라우저에서 자동으로 `http://localhost:8501`이 열립니다.

---

## 📦 웹 배포 방법 (Streamlit Cloud)

### 1단계: GitHub 저장소 준비 (5분)
```bash
# 프로젝트 폴더로 이동
cd "/Users/HuiJune Park/I AI/Cursor/Project/Market Signal/Market Risk"

# Git 초기화 (처음 한 번만)
git init
git add .
git commit -m "Initial commit"
git branch -M main

# GitHub에서 새 저장소 생성 후 아래 명령어 실행
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
git push -u origin main
```

### 2단계: Streamlit Cloud 배포 (3분)
1. **https://streamlit.io/cloud** 접속 → GitHub 계정으로 로그인
2. **"New app"** 클릭
3. 설정:
   - **Repository**: 방금 만든 GitHub 저장소 선택
   - **Branch**: `main`
   - **Main file path**: `main.py`
4. **"Advanced settings"** → **"Secrets"** 탭 클릭
5. 다음 내용 입력:
   ```toml
   FRED_API_KEY = "3c135ee62b5baa4f41adcf37a4a508c9"
   ```
6. **"Save"** → **"Deploy!"** 클릭

### 3단계: 완료! 🎉
배포가 완료되면 (약 2-3분) Streamlit Cloud에서 제공하는 URL로 접근 가능합니다.
예: `https://your-app-name.streamlit.app`

**이제 어디서든 인터넷만 있으면 앱을 사용할 수 있습니다!**

---

## 📱 사용 방법

### 주요 기능
1. **S&P 500 & VIX**: 주식 시장 지수와 변동성 지수 확인
2. **High Yield Spread**: 고수익 채권 스프레드 모니터링
3. **SOFR & US 10-Year Bond Yield**: 금리와 채권 수익률 추적
4. **기타 지표들**: 다양한 시장 지표 분석

### 사용 팁
- **날짜 선택**: 각 섹션에서 시작일/종료일을 선택하여 원하는 기간의 데이터 확인
- **Period 선택**: 1일, 1주, 1개월, 1년 등 빠른 기간 선택 가능
- **인터랙티브 그래프**: Plotly 그래프로 확대/축소, 호버 정보 확인 가능

---

## 🔄 업데이트 방법

코드를 수정한 후:
```bash
git add .
git commit -m "Update dashboard"
git push
```
Streamlit Cloud가 자동으로 재배포합니다 (약 1-2분 소요).

---

## 💡 참고사항

- **무료 사용**: Streamlit Cloud 무료 플랜으로도 사용 가능
- **자동 업데이트**: GitHub에 푸시하면 자동으로 재배포
- **API 키 보안**: API 키는 Streamlit Cloud의 Secrets에 안전하게 저장됨




