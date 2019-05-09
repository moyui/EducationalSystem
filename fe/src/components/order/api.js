import api from '../../api';

const URL = {
  ORDERLIST: '/orderList'
};

function getOrderList() {
  return api({
    url: URL.ORDERLIST,
    method: 'get'
  });
}

export { getOrderList };