import api from '../../api';

const URL = {
  PURCHASE: '/shop/purchase'
};

function postPurchase(id, link) {
  return api({
    url: URL.PURCHASE,
    method: 'post',
    data: {
      id,
      payway: 1,
      link
    }
  });
}

export { postPurchase };
