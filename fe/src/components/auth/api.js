import api from '../../api';

const URL = {
  LOGIN: '/login',
  REGISTER: '/register'
};

function postLogin({ mail, password }) {
  return api({
    method: 'post',
    url: URL.LOGIN,
    data: {
      mail,
      password
    }
  });
}

function postRegister({ mail, password, userName }) {
  return api({
    method: 'post',
    url: URL.REGISTER,
    data: {
      mail,
      password,
      userName
    }
  });
}

export { postLogin, postRegister };
