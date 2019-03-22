import api from '../../api';

const URL = {
  VIDEO: '/video'
};

function getVideo({ videoid, courseid }) {
  return api({
    url: URL.VIDEO,
    method: 'get',
    params: {
      videoid,
      courseid
    }
  });
}

export { getVideo };
