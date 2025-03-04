import { Button } from "@/components/ui/button"
import { MoreHorizontal,Share,Pencil,Trash2  } from 'lucide-react';
import {
    DropdownMenu,
    DropdownMenuTrigger,
    DropdownMenuContent,
    DropdownMenuItem,
  } from "@/components/ui/dropdown-menu"

export default function Counter() {
    return (
        
        <div id="bolu" className="w-full flex justify-between items-center bg-black text-white hover:bg-gray-300 px-4 py-2 rounded-lg cursor-pointer">
            <a href={props.link} className="w-full flex text-left no-underline" style={{ maxWidth: "calc(100% - 24px)" }}>
                <span className="truncate" style={{ maxWidth: "calc(100% - 24px)" }}>
                {props.name}
                </span>
            </a>
            <DropdownMenu>
                <DropdownMenuTrigger asChild>
                <MoreHorizontal className="h-4 w-4 opacity-60 ml-2 cursor-pointer" />
                </DropdownMenuTrigger>
                <DropdownMenuContent side="top" align="end" className="w-[--radix-popper-anchor-width]">
                <DropdownMenuItem>
                    <Share /><span>Share</span>
                </DropdownMenuItem>
                <DropdownMenuItem>
                    <Pencil /><span>Rename</span>
                </DropdownMenuItem>
                <DropdownMenuItem id="drop-delete">
                    <Trash2 /><span>Delete</span>
                </DropdownMenuItem>
                </DropdownMenuContent>
            </DropdownMenu>
        </div>  
    );
}