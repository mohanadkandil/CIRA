import { Button } from "@/components/ui/button";
import {
  Dialog,
  DialogContent,
  DialogDescription,
  DialogFooter,
  DialogHeader,
  DialogTitle,
  DialogTrigger,
} from "@/components/ui/dialog";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import { Textarea } from "@/components/ui/textarea";
import Image from "next/image";

export default function Home() {
  return (
    <main className="flex min-h-screen bg-white flex-col items-center justify-center p-24">
      <div className="w-full h-full flex items-center justify-center gap-8">
        <button className="rounded-xl border-2 bg-green-300 px-24 py-24">
          <BookIcon className="w-32 h-32" />
        </button>
        <button className="rounded-xl border-2 bg-green-300 px-24 py-24">
          <SleepingIcon className="w-32 h-32" />
        </button>
      </div>
      <Dialog>
        <DialogTrigger asChild>
          <Button variant="secondary" color="#" className="mt-8">
            Add a new mode
          </Button>
        </DialogTrigger>
        <DialogContent className="sm:max-w-[490px]">
          <DialogHeader>
            <DialogTitle>Craft Your Own Mode</DialogTitle>
            <DialogDescription>
              Just write down what mode do you need and your target group!
            </DialogDescription>
          </DialogHeader>
          <div className="grid gap-4 py-4">
            <div className="grid grid-cols-4 items-center gap-4">
              <Label htmlFor="name" className="text-right">
                Target Group
              </Label>
              <Input
                id="name"
                defaultValue="Pedro Duarte"
                className="col-span-3"
              />
            </div>
            <div className="grid grid-cols-4 items-center gap-4">
              <Label htmlFor="prompt" className="text-right">
                Your prompt
              </Label>
              <Textarea
                placeholder="Type your prompt here."
                id="prompt"
                className="w-[300px]"
              />
            </div>
          </div>
          <DialogFooter>
            <Button type="submit">Generate</Button>
          </DialogFooter>
        </DialogContent>
      </Dialog>
    </main>
  );
}

const BookIcon = (props) => (
  <svg
    xmlns="http://www.w3.org/2000/svg"
    width={800}
    height={800}
    fill="none"
    viewBox="0 0 24 24"
    {...props}
  >
    <path
      fill="#1C274D"
      d="M12 20.028V18H8v2.028c0 .277 0 .416.095.472.095.056.224-.006.484-.13l1.242-.593c.088-.042.132-.063.179-.063.047 0 .091.02.179.063l1.242.593c.26.124.39.186.484.13.095-.056.095-.195.095-.472Z"
      opacity={0.5}
    />
    <path
      fill="#1C274D"
      d="M8 18h-.574c-1.084 0-1.462.006-1.753.068-.513.11-.96.347-1.285.667-.11.108-.164.161-.291.505-.127.343-.107.489-.066.78l.022.15c.11.653.31.998.616 1.244.307.246.737.407 1.55.494.837.09 1.946.092 3.536.092h4.43c1.59 0 2.7-.001 3.536-.092.813-.087 1.243-.248 1.55-.494.306-.246.506-.591.616-1.243.091-.548.11-1.241.113-2.171h-8v2.028c0 .277 0 .416-.095.472-.095.056-.224-.006-.484-.13l-1.242-.593c-.088-.042-.132-.063-.179-.063-.047 0-.091.02-.179.063l-1.242.593c-.26.124-.39.186-.484.13C8 20.444 8 20.305 8 20.028V18Z"
    />
    <path
      fill="#1C274D"
      d="M4.727 2.733c.306-.308.734-.508 1.544-.618C7.105 2.002 8.209 2 9.793 2h4.414c1.584 0 2.688.002 3.522.115.81.11 1.238.31 1.544.618.305.308.504.74.613 1.557.112.84.114 1.955.114 3.552V18H7.426c-1.084 0-1.462.006-1.753.068-.513.11-.96.347-1.285.667-.11.108-.164.161-.291.505A1.273 1.273 0 0 0 4 19.7V7.842c0-1.597.002-2.711.114-3.552.109-.816.308-1.249.613-1.557Z"
      opacity={0.5}
    />
    <path
      fill="#1C274D"
      d="M7.25 7A.75.75 0 0 1 8 6.25h8a.75.75 0 0 1 0 1.5H8A.75.75 0 0 1 7.25 7ZM8 9.75a.75.75 0 0 0 0 1.5h5a.75.75 0 0 0 0-1.5H8Z"
    />
  </svg>
);

const SleepingIcon = (props) => (
  <svg
    xmlns="http://www.w3.org/2000/svg"
    width={800}
    height={800}
    fill="none"
    viewBox="0 0 24 24"
    {...props}
  >
    <path
      stroke="#1C274C"
      strokeLinecap="round"
      strokeWidth={1.5}
      d="M6.5 11c.567.63 1.256 1 2 1s1.433-.37 2-1M13.5 11c.567.63 1.256 1 2 1s1.433-.37 2-1"
    />
    <path fill="#1C274C" d="M13 16a1 1 0 1 1-2 0 1 1 0 0 1 2 0Z" />
    <path
      stroke="#1C274C"
      strokeLinecap="round"
      strokeLinejoin="round"
      strokeWidth={1.5}
      d="m17 4 3.464-2L19 7.464l3.464-2M14.048 5.5l1.732 1-2.732.732 1.732 1"
    />
    <path
      stroke="#1C274C"
      strokeLinecap="round"
      strokeWidth={1.5}
      d="M22 12c0 5.523-4.477 10-10 10a9.955 9.955 0 0 1-5-1.338M12 2C6.477 2 2 6.477 2 12c0 1.821.487 3.53 1.338 5"
    />
  </svg>
);
