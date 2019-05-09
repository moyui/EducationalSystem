import api from '../../api';

const URL = {
  PAYWAY: '/shop/payway',
  RECHAREG: '/shop/recharge',
  USERINFO: '/userinfo',
  RESTLIST: '/shop/restList'
};

function getPayWay() {
  return api({
    url: URL.PAYWAY,
    method: 'get'
  });
}

function postRecharge({ payway, amount }) {
  return api({
    url: URL.RECHAREG,
    method: 'post',
    data: {
      payway,
      amount
    }
  });
}

function getUserInfo() {
    return api({
        url: URL.USERINFO,
        method: 'get'
    })
}

function getRestList() {
    return api({
        url: URL.RESTLIST,
        method: 'get'
    })
}

export { getPayWay, postRecharge, getUserInfo, getRestList };
