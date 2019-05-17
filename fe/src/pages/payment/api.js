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
      payway: 2,
      link
    }
  });
}

export { postPurchase };
