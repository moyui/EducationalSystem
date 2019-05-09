import api from '../../api';

const URL = {
  VIDEO: '/video',
  PROGRESS: '/progress'
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

function postProgress({ videoid, courseid }) {
  return api({
    url: URL.PROGRESS,
    method: 'post',
    data: {
      videoid,
      courseid
    }
  });
}

export { getVideo, postProgress };
