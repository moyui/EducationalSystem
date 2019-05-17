import api from '../../api';

const URL = {
  USERINFO: '/userinfo'
};

function getUserInfo() {
    return api({
        url: URL.USERINFO,
        method: 'get'
    })
}

export { getUserInfo }