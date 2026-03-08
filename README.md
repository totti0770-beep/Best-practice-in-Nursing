🩺 Best Nursing Practice AI — Backend
نظام ذكاء اصطناعي متخصص للممارسين الصحيين والتمريض، يعتمد على RAG (Retrieval-Augmented Generation) لتحليل مستندات المستخدم والإجابة على الأسئلة اعتمادًا على محتوى المستندات فقط.
________________________________________
⭐ المزايا الرئيسية
•	رفع ملفات PDF واستخراج النص منها تلقائيًا
•	تقسيم النص إلى أجزاء (Chunks) وتحويلها إلى Embeddings
•	تخزين المتجهات في Pinecone للبحث الدلالي
•	استخدام Supabase لتخزين المستخدمين، المستندات، الجلسات، والرسائل
•	محرك ذكاء اصطناعي (OpenAI GPT 4o) للإجابة على الأسئلة
•	دعم الاستشهادات (Citations) مع كل إجابة
•	دعم إعدادات المستخدم (اللغة، التخصص، مستوى التفاصيل)
•	دعم Feedback لتحسين جودة الإجابات
•	هيكلية نظيفة وقابلة للتوسع
________________________________________
📁 هيكلية المشروع
best-nursing-ai-backend/
│
├── app/
│   ├── main.py
│   ├── config.py
│   ├── database.py
│   ├── auth.py
│   │
│   ├── models/
│   │   └── schemas.py
│   │
│   ├── routes/
│   │   ├── auth.py
│   │   ├── documents.py
│   │   ├── chat.py
│   │   ├── feedback.py
│   │   └── users.py
│   │
│   ├── services/
│   │   ├── pdf_processor.py
│   │   ├── embedding.py
│   │   ├── vector_store.py
│   │   └── llm.py
│   │
│   └── utils/
│       └── helpers.py
│
├── tests/
│
├── .env.example
├── requirements.txt
├── README.md
└── .gitignore
________________________________________
🔧 المتطلبات
Python 3.10+
مكتبات Python (requirements.txt)
fastapi[all]==0.104.1
uvicorn[standard]==0.24.0
python-dotenv==1.0.0
supabase==1.2.0
pinecone-client==3.0.0
openai==1.3.0
pypdf2==3.0.1
pdfplumber==0.10.3
langchain==0.0.340
langchain-text-splitters==0.0.0
httpx==0.25.1
python-multipart==0.0.6
pydantic==2.5.0
PyJWT==2.8.0
________________________________________
🔐 ملف البيئة .env
استخدم هذا النموذج:
SUPABASE_URL=
SUPABASE_KEY=
SUPABASE_JWT_SECRET=

PINECONE_API_KEY=
PINECONE_ENVIRONMENT=
PINECONE_INDEX_NAME=

OPENAI_API_KEY=
________________________________________
▶️ تشغيل المشروع محليًا
1) تثبيت المتطلبات
pip install -r requirements.txt
2) تشغيل السيرفر
uvicorn app.main:app --reload
3) واجهة التوثيق (Swagger)
http://127.0.0.1:8000/docs
________________________________________
🚀 النشر على Render (أسهل طريقة)
1) ارفع المشروع على GitHub
2) ادخل https://render.com
3) أنشئ Web Service جديد
4) إعدادات التشغيل:
Start Command
uvicorn app.main:app --host 0.0.0.0 --port 10000
Environment Variables 
انسخ محتوى .env.example
بعد النشر سيظهر رابط مثل:
https://best-nursing-ai.onrender.com/api/v1
________________________________________
🧠 كيف يعمل النظام (RAG Pipeline)
1) رفع المستند
•	يتم حفظه في Supabase Storage
•	يتم إنشاء سجل في جدول documents
2) استخراج النص
•	باستخدام pdfplumber
3) تقسيم النص
•	باستخدام RecursiveCharacterTextSplitter
4) إنشاء Embeddings
•	باستخدام OpenAI text-embedding-3-large
5) تخزين المتجهات
•	في Pinecone
•	namespace = user_id
6) عند طرح سؤال
•	يتم تحويل السؤال إلى embedding
•	البحث في Pinecone
•	جلب أفضل 5 chunks
•	إرسالها إلى GPT 4o مع السؤال
•	توليد الإجابة + الاستشهادات
________________________________________
📡 API Endpoints
🔐 Auth
•	POST /api/v1/auth/register
•	POST /api/v1/auth/login
📄 Documents
•	POST /api/v1/documents/upload
•	GET /api/v1/documents
•	DELETE /api/v1/documents/{id}
💬 Chat
•	POST /api/v1/chat/sessions
•	GET /api/v1/chat/sessions
•	POST /api/v1/chat/sessions/{id}/messages
⭐ Feedback
•	POST /api/v1/feedback
👤 Users
•	GET /api/v1/users/me
•	PATCH /api/v1/users/settings
•	DELETE /api/v1/users/data

