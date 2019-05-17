import api from '../../api';

const URL = {
  ANSWER: '/answer',
  QUESTION: '/question'
};

function getQuestion(courseid, type, videoid) {
  return api({
    url: URL.QUESTION,
    method: 'get',
    params: {
      courseid,
      videoid,
      type
    }
  });
}

function postAnswer(courseid, testid, answer) {
  return api({
    url: URL.ANSWER,
    method: 'post',
    data: {
      courseid,
      testid,
      answer
    }
  });
}

export { postAnswer, getQuestion };
