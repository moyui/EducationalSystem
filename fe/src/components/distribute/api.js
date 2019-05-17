import api from '../../api';

const URL = {
    GETDISTRIBUTE: '/getdistribution',
    CANCELDISTRIBUTE: '/closedistribution'
};

function getDistribution() {
  return api({
    url: URL.GETDISTRIBUTE,
    method: 'get'
  });
}

function closeDistribution(id) {
  return api({
    url: URL.CANCELDISTRIBUTE,
    method: 'post',
    data: {
      id
    }
  });
}


export { getDistribution, closeDistribution }