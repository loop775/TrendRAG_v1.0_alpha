from langchain.chat_models import ChatOpenAI
from langchain.chains.question_answering import load_qa_chain
from langchain.prompts import PromptTemplate

llm = ChatOpenAI(temperature=0.2)
prompt_template = PromptTemplate.from_template(
    """Given the following user post: {post}\n
And the following current trending topics: {trends}\n
Explain whether this post is likely to trend and why."""
)

qa_chain = load_qa_chain(llm=llm, chain_type="stuff", prompt=prompt_template)

def generate_rag_response(post, trends):
    context = "\n".join([t.page_content for t in trends])
    return qa_chain.run({"post": post, "trends": context})