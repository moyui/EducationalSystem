import api from '../../api';

const URL = {
  LOGIN: '/login',
  REGISTER: '/register'
};

function postLogin({ phone, password }) {
  return api({
    method: 'post',
    url: URL.LOGIN,
    data: {
      phone,
      password
    }
  });
}

function postRegister({ phone, password }) {
  return api({
    method: 'post',
    url: URL.REGISTER,
    data: {
      phone,
      password
    }
  });
}

export { postLogin, postRegister };
