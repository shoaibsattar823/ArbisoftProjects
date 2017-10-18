import axios from 'axios';

// actions
export const ADD_BLOG = 'ADD_BLOG';
export const FETCH_BLOGS = 'FETCH_BLOGS';
export const EDIT_BLOG = 'EDIT_BLOG';
export const FETCH_BLOG_DETAIL = 'FETCH_BLOG_DETAIL';


const ROOT_URL = "http://localhost:8000";

export function fetchBlogs(){
  const url = `${ROOT_URL}/blogs/?format=json`;
  // const url = 'http://api.openweathermap.org/data/2.5/forecast?q=Skardu,us&appid=3f4be8e2d6926fad51510a2874891677';
  const request = axios.get(url);

  return {
    type: FETCH_BLOGS,
    payload: request
  };
}


export function fetchBlogDetail(title) {
  const url = `${ROOT_URL}/blogs/${title}/?format=json`;
  const request = axios.get(url);
  return {
    type: FETCH_BLOG_DETAIL,
    payload: request
  };
}
