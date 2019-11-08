import java.io.IOException;
import java.util.StringTokenizer;

import java.util.HashSet;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.Mapper;
import org.apache.hadoop.mapreduce.Reducer;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.input.MultipleInputs;
import org.apache.hadoop.mapreduce.lib.input.TextInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;

public class Join {

  public static class Rmapper extends Mapper<Object, Text, Text, Text> 
  {
    public void map(Object key, Text value, Context context) throws IOException, InterruptedException 
    {
      String record = value.toString();
      String[] parts = record.split(" ");
      Float i=new Float(parts[2]);
      if(i>4.0)
      context.write(new Text(parts[0]), new Text(parts[2]+" "+parts[1]));
    }
  }

  


  // REDUCE
  public static class JoinReducer extends Reducer<Text, Text, Text, Text> {

    public void reduce(Text key, Iterable<Text> values, Context context) throws IOException, InterruptedException {

      HashSet<String> Rtable = new HashSet<>();

   //   Rtable.add("rTeste");
 //     Stable.add("sTeste");
      for (Text val : values) {
        String parts[] = val.toString().split(" ");
          Rtable.add(parts[1]);
         
      }

      for (String r: Rtable)  {
    	  for (String v: Rtable) {
    		  if(v!=r)
    		  context.write(new Text("<"+v+","+r+">"), new Text(" "));
    	  }
      }

    }
  }
  


  public static void main(String[] args) throws Exception {
    Configuration conf = new Configuration();
    Job job = Job.getInstance(conf, "join");
    job.setJarByClass(Join.class);

    // INPUT and MAP
    MultipleInputs.addInputPath(job, new Path(args[0]),TextInputFormat.class, Rmapper.class);
      
    // REDUCE
    job.setReducerClass(JoinReducer.class); 
   
    //OUTPUT
    job.setOutputKeyClass(Text.class);
    job.setOutputValueClass(Text.class);

    FileOutputFormat.setOutputPath(job, new Path(args[1]));
    System.exit(job.waitForCompletion(true) ? 0 : 1);
  }
}
