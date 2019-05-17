import api from '../../api';

const URL = {
  USERINFO: '/userinfo',
  PHONE: '/phone',
  HONER: '/honer'
};

function getInfo() {
  return api({
    url: URL.USERINFO,
    method: 'get'
  });
}

function postPhone(phone) {
  return api({
    url: URL.PHONE,
    method: 'post',
    data: {
      phone
    }
  });
}

function getHoner() {
  return api({
    url: URL.HONER,
    method: 'get'
  });
}

export { getInfo, postPhone, getHoner };
