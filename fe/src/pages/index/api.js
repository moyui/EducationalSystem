import api from '../../api';

const URL = {
  CLASSIFY: '/course/classify',
  List: '/course/list'
};

function getClassify() {
  return api({
    url: URL.CLASSIFY,
    method: 'get'
  });
}

function getList(varietyid) {
  return api({
    url: URL.List,
    method: 'get',
    params: {
      varietyid
    }
  });
}

export { getClassify, getList };
