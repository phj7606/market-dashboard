# Streamlit Cloud 배포 가이드

이 가이드는 Market Risk Dashboard를 Streamlit Cloud에 배포하는 방법을 설명합니다.

## 배포 전 준비사항

### 1. GitHub 저장소 생성 및 업로드

1. GitHub에 새 저장소를 생성합니다.
2. 프로젝트 폴더를 Git 저장소로 초기화하고 GitHub에 푸시합니다:

```bash
cd "/Users/HuiJune Park/I AI/Cursor/Project/Market Signal/Market Risk"
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
git push -u origin main
```

### 2. Streamlit Cloud 배포

1. [Streamlit Cloud](https://streamlit.io/cloud)에 접속하여 로그인합니다.
2. "New app" 버튼을 클릭합니다.
3. GitHub 저장소를 선택합니다.
4. 배포 설정:
   - **Main file path**: `main.py`
   - **Python version**: 3.9 이상
   - **Branch**: `main` (또는 원하는 브랜치)

### 3. Secrets 설정 (API 키)

Streamlit Cloud 대시보드에서:
1. 앱 설정으로 이동
2. "Secrets" 탭 클릭
3. 다음 형식으로 secrets 추가:

```toml
FRED_API_KEY = "3c135ee62b5baa4f41adcf37a4a508c9"
```

또는 환경 변수로 설정:
- Settings → Secrets → Environment variables
- `FRED_API_KEY` = `your_api_key_here`

### 4. 배포 확인

배포가 완료되면 Streamlit Cloud에서 제공하는 URL로 앱에 접근할 수 있습니다.
예: `https://your-app-name.streamlit.app`

## 로컬에서 테스트

배포 전에 로컬에서 환경 변수를 설정하여 테스트할 수 있습니다:

```bash
# macOS/Linux
export FRED_API_KEY="your_api_key_here"
streamlit run main.py

# Windows
set FRED_API_KEY=your_api_key_here
streamlit run main.py
```

## 주의사항

- API 키는 절대 코드에 하드코딩하지 마세요.
- GitHub에 푸시하기 전에 `.gitignore`에 `.streamlit/secrets.toml`이 포함되어 있는지 확인하세요.
- Streamlit Cloud는 무료 플랜에서도 사용 가능하지만, 일일 사용 시간 제한이 있을 수 있습니다.

## 업데이트

코드를 수정한 후 GitHub에 푸시하면 Streamlit Cloud가 자동으로 재배포합니다.

```bash
git add .
git commit -m "Update dashboard"
git push
```

