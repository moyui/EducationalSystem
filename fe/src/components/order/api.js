import api from '../../api';

const URL = {
  ORDERLIST: '/orderList',
  DISTRIBUTE: '/distribution',
  WITHDRAW: '/withdraw'
};

function getOrderList() {
  return api({
    url: URL.ORDERLIST,
    method: 'get'
  });
}

function distribute(id) {
  return api({
    url: URL.DISTRIBUTE,
    method: 'post',
    data: {
      id
    }
  });
}

function withdraw(id) {
  return api({
    url: URL.WITHDRAW,
    method: 'post',
    data: {
      id
    }
  });
}

export { getOrderList, distribute, withdraw };