FROM public.ecr.aws/lambda/python:3.9-x86_64

COPY OpenAI.json apple_short.pdf 
COPY ./ app.py ${LAMBDA_TASK_ROOT}

RUN  \
    yum -y update && \
    yum install -y \
    libXext \
    libSM \
    libXrender \
    libgomp1 \
    yum clean all && rm -rf /var/cache/yum/*

COPY requirements.txt ./requirements.txt
RUN pip install -r requirements.txt --target "${LAMBDA_TASK_ROOT}"

CMD ["app.lambda_handler"]