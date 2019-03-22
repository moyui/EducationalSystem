import api from '../../api';

const URL = {
  VIEW: '/course/view',
  ORDER: '/shop/order',
  GETCOMMENT: '/comment/course/get',
  SENDCOMMENT: '/comment/course/send'
};

function getView(id) {
  return api({
    url: URL.VIEW,
    method: 'get',
    params: {
      id
    }
  });
}

function postOrder(id) {
  return api({
    url: URL.ORDER,
    method: 'post',
    data: {
      id
    }
  });
}

function getComment(id) {
  return api({
    url: URL.GETCOMMENT,
    method: 'get',
    params: {
      id
    }
  });
}

function postComment({ courseid, comment }) {
  return api({
    url: URL.SENDCOMMENT,
    method: 'post',
    data: {
      courseid,
      comment,
      isadd: false,
      addbelongid: -1
    }
  });
}

export { getView, postOrder, getComment, postComment };
