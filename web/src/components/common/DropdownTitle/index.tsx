import { KeyboardArrowDownRounded } from "@mui/icons-material";
import React, { ChangeEventHandler } from "react";

type DropdownTitleProps = {
  label?: string;
  placeholder?: string;
  value?: string;
  options?: any[];
  isOpen: boolean;
  toggle: () => void;
  error?: boolean;
  showIcon?: boolean;
  disabled?: boolean;
  inputDisabed?: boolean;
  onChange?: ChangeEventHandler;
  className?: string;
};

function DropdownTitle({
  placeholder,
  label,
  value,
  isOpen,
  toggle,
  error,
  showIcon = false,
  disabled = false,
  inputDisabed = false,
  onChange = () => {},
  className,
}: DropdownTitleProps) {
  return (
    <div
      onClick={() => (disabled ? () => {} : toggle())}
      style={{
        backgroundColor: disabled ? "#efefef" : "",
      }}
      className={`${
        error ? "border-red-500" : ""
      } flex items-center gap-2 justify-between w-full rounded border p-2 bg-white text-xs font-medium text-gray-700 focus:outline-none overflow-hidden cursor-pointer`}>
      <input
        className={`${className} w-full h-full rounded outline-none max-w-full min-w-[200px] font-medium text-ellipsis disabled:bg-transparent`}
        type="text"
        placeholder={placeholder ?? `Select ${label}`}
        value={value}
        disabled={inputDisabed}
        onChange={onChange}
      />
      {showIcon && (
        <KeyboardArrowDownRounded
          fontSize="small"
          className={`${
            isOpen ? "rotate-180" : "rotate-0"
          } text-gray-600 !transition-all`}
        />
      )}
    </div>
  );
}

export default DropdownTitle;
