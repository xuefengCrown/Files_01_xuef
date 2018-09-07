package algs.implebyme.sorting;

import algs.base.In;
import algs.base.StdOut;
// 归并多个输入流（降序）
public class Multiway
{
	public static void merge(In[] streams)
	{
		int N = streams.length;
		IndexMaxPQ<String> pq = new IndexMaxPQ<String>(N);
		for (int i = 0; i < N; i++)
			if (!streams[i].isEmpty())
				pq.insert(i, streams[i].readString());
		while (!pq.isEmpty())
		{
			StdOut.println(pq.max());
			int i = pq.delMax();
			if (!streams[i].isEmpty())
				pq.insert(i, streams[i].readString());
		}
	}
	public static void main(String[] args)
	{
		int N = args.length;
		In[] streams = new In[N];
		for (int i = 0; i < N; i++)
			streams[i] = new In(args[i]);
		merge(streams);
	}
}
