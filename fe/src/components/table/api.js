import api from '../../api';

const URL = {
  TABLE: '/course/table'
};

function getTable() {
  return api({
    url: URL.TABLE,
    method: 'get'
  });
}

export { getTable };
