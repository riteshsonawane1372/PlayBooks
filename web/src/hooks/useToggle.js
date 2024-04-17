import { useState } from 'react';

const useToggle = (initialState = false) => {
  const [isOpen, setIsOpen] = useState(initialState);
  const toggle = newVal => {
    typeof newVal === 'boolean' ? setIsOpen(newVal) : setIsOpen(!isOpen);
  };
  return { isOpen, toggle };
};

export default useToggle;
